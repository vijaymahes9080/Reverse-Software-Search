from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
import json
import io

from app.config import settings
from app.database import engine, Base, get_db
from app.models.blueprint import Blueprint
from app.engines.synthesis_pipeline import synthesize_product
from app.engines.repo_generator import create_zip_archive
from app.services.genome_data import GENOME_DATABASE
from app.services.capability_graph import capability_graph

# Initialize database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI software synthesis engine that generates full engineering blueprints from natural language prompts."
)

from app.services.security import SecurityHeadersMiddleware

# Configure CORS & Security Headers
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow development frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.services.telemetry import get_telemetry_status, record_synthesis

@app.get("/")
def read_root():
    return {
        "status": "online",
        "app": settings.PROJECT_NAME,
        "version": settings.VERSION
    }

@app.get("/api/v1/health")
def get_health_status():
    """Retrieve system health and telemetry metrics."""
    return get_telemetry_status()

@app.get("/api/v1/genomes")
def get_genomes():
    """Retrieve all seeded software genomes."""
    return list(GENOME_DATABASE.values())

@app.get("/api/v1/capability-graph")
def get_full_capability_graph():
    """Retrieve the entire system capability graph."""
    return capability_graph.get_subgraph(list(capability_graph.G.nodes()))

@app.post("/api/v1/synthesize")
def run_synthesis(payload: dict, db: Session = Depends(get_db)):
    """
    Synthesize an entire product from a natural language prompt.
    """
    prompt = payload.get("prompt")
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
        
    try:
        blueprint_data = synthesize_product(prompt)
        
        # Save to database
        db_blueprint = Blueprint(
            id=blueprint_data["id"],
            prompt=blueprint_data["prompt"],
            title=blueprint_data["title"],
            tagline=blueprint_data["tagline"],
            summary=blueprint_data["summary"],
            intent_json=json.dumps(blueprint_data["intent"]),
            genome_json=json.dumps(blueprint_data["genomes"]),
            graph_json=json.dumps(blueprint_data["graph"]),
            architecture_json=json.dumps(blueprint_data["architecture"]),
            ui_json=json.dumps(blueprint_data["ui"]),
            db_json=json.dumps(blueprint_data["db"]),
            api_json=json.dumps(blueprint_data["apis"]),
            ai_json=json.dumps(blueprint_data["ai"]),
            workflow_json=json.dumps(blueprint_data["workflows"]),
            deployment_json=json.dumps(blueprint_data["deployment"]),
            cost_json=json.dumps(blueprint_data["costs"]),
            oss_json=json.dumps(blueprint_data["oss"]),
            innovation_json=json.dumps(blueprint_data["innovations"]),
            startup_json=json.dumps(blueprint_data["startup"]),
            files_json=json.dumps(blueprint_data["files"]),
            multi_agent_json=json.dumps(blueprint_data.get("multi_agent", {}))
        )
        
        db.add(db_blueprint)
        db.commit()
        db.refresh(db_blueprint)
        
        return blueprint_data
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Synthesis failed: {str(e)}")

@app.get("/api/v1/blueprints")
def list_blueprints(db: Session = Depends(get_db)):
    """List all previously synthesized products."""
    blueprints = db.query(Blueprint).order_by(Blueprint.created_at.desc()).all()
    return [
        {
            "id": bp.id,
            "prompt": bp.prompt,
            "title": bp.title,
            "tagline": bp.tagline,
            "summary": bp.summary,
            "created_at": bp.created_at
        }
        for bp in blueprints
    ]

@app.get("/api/v1/blueprints/{blueprint_id}")
def get_blueprint(blueprint_id: str, db: Session = Depends(get_db)):
    """Retrieve detailed specs for a specific blueprint."""
    bp = db.query(Blueprint).filter(Blueprint.id == blueprint_id).first()
    if not bp:
        raise HTTPException(status_code=404, detail="Blueprint not found")
        
    return {
        "id": bp.id,
        "prompt": bp.prompt,
        "title": bp.title,
        "tagline": bp.tagline,
        "summary": bp.summary,
        "created_at": bp.created_at,
        "intent": json.loads(bp.intent_json),
        "genomes": json.loads(bp.genome_json),
        "graph": json.loads(bp.graph_json),
        "architecture": json.loads(bp.architecture_json),
        "db": json.loads(bp.db_json),
        "apis": json.loads(bp.api_json),
        "ui": json.loads(bp.ui_json),
        "workflows": json.loads(bp.workflow_json),
        "ai": json.loads(bp.ai_json),
        "deployment": json.loads(bp.deployment_json),
        "costs": json.loads(bp.cost_json),
        "oss": json.loads(bp.oss_json),
        "innovations": json.loads(bp.innovation_json),
        "startup": json.loads(bp.startup_json),
        "files": json.loads(bp.files_json),
        "multi_agent": json.loads(bp.multi_agent_json) if bp.multi_agent_json else {}
    }

@app.get("/api/v1/blueprints/{blueprint_id}/multi-agent-review")
def get_multi_agent_review(blueprint_id: str, db: Session = Depends(get_db)):
    """Retrieve Multi-Agent Engineering Council Assessment for a specific blueprint."""
    bp = db.query(Blueprint).filter(Blueprint.id == blueprint_id).first()
    if not bp:
        raise HTTPException(status_code=404, detail="Blueprint not found")
    return json.loads(bp.multi_agent_json) if bp.multi_agent_json else {}

@app.get("/api/v1/blueprints/{blueprint_id}/download")
def download_blueprint_zip(blueprint_id: str, db: Session = Depends(get_db)):
    """Compile and export the repository codefiles as a zipped folder download."""
    bp = db.query(Blueprint).filter(Blueprint.id == blueprint_id).first()
    if not bp:
        raise HTTPException(status_code=404, detail="Blueprint not found")
        
    files = json.loads(bp.files_json)
    zip_bytes = create_zip_archive(files)
    
    return StreamingResponse(
        io.BytesIO(zip_bytes),
        media_type="application/zip",
        headers={
            "Content-Disposition": f"attachment; filename={bp.title.lower().replace(' ', '_')}_starter.zip"
        }
    )


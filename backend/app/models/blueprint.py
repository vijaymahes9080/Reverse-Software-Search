import datetime
from sqlalchemy import Column, String, Text, DateTime
from app.database import Base

class Blueprint(Base):
    __tablename__ = "blueprints"

    id = Column(String, primary_key=True, index=True)
    prompt = Column(String, index=True)
    title = Column(String, index=True)
    tagline = Column(String)
    summary = Column(Text)
    
    # Store JSON structures as Text/JSON
    intent_json = Column(Text)         # Intent extraction results
    genome_json = Column(Text)         # Matched genome traits
    graph_json = Column(Text)          # Capability Graph structure
    architecture_json = Column(Text)   # Services, systems, diagrams
    ui_json = Column(Text)             # Screen definitions, shadcn theme, layouts
    db_json = Column(Text)             # ER diagrams, SQL DDL schema, tables
    api_json = Column(Text)            # OpenAPI, REST endpoints, webhooks
    ai_json = Column(Text)             # Prompt chain, agents, model routing
    workflow_json = Column(Text)       # User journey map, sequence diagram
    deployment_json = Column(Text)     # Dockerfile, Docker Compose, CI/CD Actions, K8s configs
    cost_json = Column(Text)           # Infrastructure & LLM cost estimates
    oss_json = Column(Text)            # Recommendations for OSS alternatives
    innovation_json = Column(Text)     # 30%+ innovations & market gaps
    startup_json = Column(Text)        # GTM, pricing tiers, pitch deck slides, SWOT
    files_json = Column(Text)          # Synthesized file content map for visual repository download
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

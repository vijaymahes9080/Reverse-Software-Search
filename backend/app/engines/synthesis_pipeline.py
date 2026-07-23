import uuid
from typing import Dict, Any, List
from app.engines.intent import extract_intent
from app.engines.genome_matcher import match_genomes
from app.services.capability_graph import capability_graph
from app.engines.architecture import generate_architecture
from app.engines.db_designer import design_database
from app.engines.api_generator import generate_apis
from app.engines.ui_generator import generate_ui
from app.engines.workflow import generate_workflows
from app.engines.ai_planner import plan_ai_features
from app.engines.deployment import plan_deployment
from app.engines.cost_analyzer import calculate_costs
from app.engines.oss import recommend_oss_alternatives
from app.engines.innovation import generate_innovations
from app.engines.startup import generate_startup_specs
from app.engines.repo_generator import generate_repository_files

def synthesize_product(prompt: str) -> Dict[str, Any]:
    """
    Master pipeline executing all 17 sub-engines to synthesize a complete blueprint.
    """
    # 1. Intent understanding
    intent = extract_intent(prompt)
    
    # 2. Genome matching
    genomes = match_genomes(prompt, intent)
    
    # 3. Capability Graph matching
    # Extract keywords from title, domain, and prompt
    keywords = prompt.split() + intent["title"].split() + intent["domain"].split()
    clean_keywords = [kw.strip("+,.-!?/\\()").lower() for kw in keywords if len(kw) > 2]
    matched_nodes = capability_graph.find_relevant_nodes(clean_keywords)
    
    # If no specific nodes matched, default to standard baseline capabilities
    if not matched_nodes:
        if "chat" in prompt.lower() or "communication" in prompt.lower():
            matched_nodes = ["pubsub_chat", "webrtc_voice", "auth_rbac"]
        elif "canvas" in prompt.lower() or "drawing" in prompt.lower():
            matched_nodes = ["drawing_canvas", "rich_text_editor", "block_storage"]
        else:
            # Canva + GitHub + Notion default mix
            matched_nodes = ["drawing_canvas", "rich_text_editor", "git_host", "workspace_hierarchy"]
            
    graph_data = capability_graph.get_subgraph(matched_nodes)
    
    # 4. Architecture planning
    architecture = generate_architecture(prompt, intent, genomes)
    
    # 5. Database Designer
    db = design_database(prompt, intent, genomes)
    
    # 6. API Generator
    apis = generate_apis(prompt, intent, genomes)
    
    # 7. UI Generator
    ui = generate_ui(prompt, intent, genomes)
    
    # 8. Workflow Generator
    workflows = generate_workflows(prompt, intent, genomes)
    
    # 9. AI Planner
    ai_plan = plan_ai_features(prompt, intent, genomes)
    
    # 10. Deployment Generator
    deployment = plan_deployment(prompt, intent, genomes)
    
    # 11. Cost Analyzer
    costs = calculate_costs(prompt, intent, genomes)
    
    # 12. Open Source Replacement Engine
    oss = recommend_oss_alternatives(genomes["matches"])
    
    # 13. Innovation Engine
    innovations = generate_innovations(prompt, intent, genomes)
    
    # 14. Startup Generator
    startup = generate_startup_specs(prompt, intent, genomes)
    
    # 15. Repository Files Generation
    files = generate_repository_files(prompt, intent, genomes, apis, db, ui)
    
    # Create final compiled result object
    blueprint_id = str(uuid.uuid4())
    
    return {
        "id": blueprint_id,
        "prompt": prompt,
        "title": intent["title"],
        "tagline": intent["tagline"],
        "summary": f"A synthesized `{intent['domain']}` combining capabilities of {', '.join(genomes['matches'])} with a custom innovation index of {innovations['innovation_index']}.",
        "intent": intent,
        "genomes": genomes,
        "graph": graph_data,
        "architecture": architecture,
        "db": db,
        "apis": apis,
        "ui": ui,
        "workflows": workflows,
        "ai": ai_plan,
        "deployment": deployment,
        "costs": costs,
        "oss": oss,
        "innovations": innovations,
        "startup": startup,
        "files": files
    }

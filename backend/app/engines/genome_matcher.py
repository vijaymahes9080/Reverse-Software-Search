from typing import Dict, Any, List
from app.services.genome_data import GENOME_DATABASE

def match_genomes(prompt: str, intent: Dict[str, Any]) -> Dict[str, Any]:
    """
    Find relevant genomes that match the description and compute overlap metrics,
    combining design languages, technologies, and traits.
    """
    prompt_lower = prompt.lower()
    matched_names = []
    
    # Simple rule based mapping
    for name, data in GENOME_DATABASE.items():
        if name in prompt_lower or any(kw in intent["tagline"].lower() or kw in intent["domain"].lower() for kw in [name, data["category"].lower()]):
            matched_names.append(name)
            
    # Default fallback if nothing matches
    if not matched_names:
        if "chat" in prompt_lower or "discord" in prompt_lower or "slack" in prompt_lower:
            matched_names = ["slack", "discord"]
        elif "canvas" in prompt_lower or "design" in prompt_lower or "figma" in prompt_lower or "canva" in prompt_lower:
            matched_names = ["canva"]
        elif "git" in prompt_lower or "code" in prompt_lower or "editor" in prompt_lower:
            matched_names = ["github", "vscode"]
        else:
            matched_names = ["notion", "github"]

    matched_genomes_data = [GENOME_DATABASE[n] for n in matched_names if n in GENOME_DATABASE]

    # Combine design languages
    # Design synthesis strategy
    synthesized_design = {
        "mode": "hybrid",
        "primary_color": "#3B82F6", # default tech blue
        "text_color": "#F3F4F6",
        "font_family": "Inter, system-ui, sans-serif",
        "ui_style": "Premium dark-mode glassmorphic cards, dynamic sidebar hubs"
    }

    if len(matched_genomes_data) == 1:
        synthesized_design.update(matched_genomes_data[0]["design_language"])
    elif len(matched_genomes_data) > 1:
        # Create a hybrid of primary colors and styles
        styles = [g["design_language"]["ui_style"] for g in matched_genomes_data]
        synthesized_design["ui_style"] = f"Merged UX: {', '.join(styles[:2])}"
        colors = [g["design_language"]["primary_color"] for g in matched_genomes_data]
        synthesized_design["primary_color"] = f"linear-gradient(135deg, {colors[0]}, {colors[1]})"

    # Merge tech stack recommendations
    frontend_stack = set()
    backend_stack = set()
    db_stack = set()

    for g in matched_genomes_data:
        stack = g.get("tech_stack", {})
        frontend_stack.update(stack.get("frontend", []))
        backend_stack.update(stack.get("backend", []))
        db_stack.update(stack.get("database", []))

    # Add standard modern additions
    frontend_stack.update(["React", "TypeScript", "TailwindCSS", "Zustand"])
    backend_stack.update(["FastAPI", "Python"])
    db_stack.update(["SQLite", "PostgreSQL"])

    return {
        "matches": [g["name"] for g in matched_genomes_data],
        "synthesized_design": synthesized_design,
        "merged_tech_stack": {
            "frontend": list(frontend_stack),
            "backend": list(backend_stack),
            "database": list(db_stack)
        },
        "strengths_retained": list(set([s for g in matched_genomes_data for s in g.get("strengths", [])])),
        "weaknesses_addressed": list(set([w for g in matched_genomes_data for w in g.get("weaknesses", [])]))
    }

from typing import Dict, Any, List

OSS_REPLACEMENTS = {
    "notion": [
        {"name": "AppFlowy", "url": "https://github.com/AppFlowy-IO/AppFlowy", "language": "Flutter/Rust", "stars": "35K+", "description": "Highly custom wiki database engine, offline-first by default"},
        {"name": "Outline", "url": "https://github.com/outline/outline", "language": "TypeScript", "stars": "20K+", "description": "Beautiful, fast wiki docs for high-scaling team workspaces"}
    ],
    "github": [
        {"name": "Forgejo", "url": "https://forgejo.org/", "language": "Go", "stars": "N/A", "description": "Lightweight self-hosted git platform focused on community federation"},
        {"name": "Gitea", "url": "https://gitea.com/", "language": "Go", "stars": "40K+", "description": "Clean, quick, low-resource git server with build Actions support"}
    ],
    "canva": [
        {"name": "Penpot", "url": "https://penpot.app/", "language": "Clojure", "stars": "25K+", "description": "Design tool built directly on SVG open web standards"},
        {"name": "Excalidraw", "url": "https://excalidraw.com/", "language": "TypeScript", "stars": "45K+", "description": "Hand-drawn style infinite whiteboard for drawing charts"}
    ],
    "slack": [
        {"name": "Mattermost", "url": "https://mattermost.com/", "language": "Go/React", "stars": "30K+", "description": "Enterprise compliance chat tool with integrated workflows"},
        {"name": "Rocket.Chat", "url": "https://rocket.chat/", "language": "JavaScript", "stars": "38K+", "description": "Omnichannel communications framework with voice support"}
    ],
    "figma": [
        {"name": "Penpot", "url": "https://penpot.app/", "language": "Clojure", "stars": "25K+", "description": "Direct collaborative design system replacement"}
    ],
    "vscode": [
        {"name": "VSCodium", "url": "https://vscodium.com/", "language": "JavaScript", "stars": "25K+", "description": "Community-led, telemetry-free binary release of VSCode"}
    ]
}

def recommend_oss_alternatives(genomes_matched: List[str]) -> List[Dict[str, Any]]:
    """
    Compile a comparative recommendation matrix of open source replacements for matched proprietary platforms.
    """
    recommendations = []
    for g in genomes_matched:
        g_lower = g.lower()
        if g_lower in OSS_REPLACEMENTS:
            for alt in OSS_REPLACEMENTS[g_lower]:
                recommendations.append({
                    "proprietary": g,
                    "alternative": alt["name"],
                    "url": alt["url"],
                    "tech": alt["language"],
                    "description": alt["description"]
                })
    
    # Add default general elements
    if not recommendations:
        recommendations.append({
            "proprietary": "General SaaS Auth",
            "alternative": "Keycloak / Authentik",
            "url": "https://www.keycloak.org/",
            "tech": "Java / Go",
            "description": "Standardized Single-Sign-On user authentication directories"
        })
        
    return recommendations

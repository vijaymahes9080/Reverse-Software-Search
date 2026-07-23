from typing import Dict, Any, List

def generate_startup_specs(prompt: str, intent: Dict[str, Any], genomes: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate product pitch, pricing tiers, GTM timelines, and a SWOT matrix.
    """
    title = intent["title"]
    
    pricing = [
        {
            "tier": "Core / Community",
            "price": "$0 (Self-Hosted)",
            "features": "Single user/Server nodes, SQLite default DB, local filesystem backups, basic document creation tools."
        },
        {
            "tier": "Standard SaaS",
            "price": "$12 per user/month",
            "features": "Managed cloud instance, real-time collaboration huddles, up to 10 workspaces, PostgreSQL hosting, basic AI auto-transcription."
        },
        {
            "tier": "Enterprise / Compliant",
            "price": "Custom / Enterprise seat",
            "features": "Dedicated secure VPC nodes, keycloak SSO, unlimited history, SOC-2 audits, custom SLA contracts, advanced vector search."
        }
    ]

    swot = {
        "strengths": [
            "100% open-source core encourages developer communities",
            "Hybrid model combines document workspaces with visual drawings and developer pipelines seamlessly"
        ],
        "weaknesses": [
            "Building multi-player collaboration sync is complex and hard to debug",
            "Initial setup requires developer expertise compared to turn-key proprietary software"
        ],
        "opportunities": [
            "Fill developer and enterprise gaps left by expensive SaaS platforms",
            "Leverage private local LLMs to target highly regulated markets (HIPAA/GDPR)"
        ],
        "threats": [
            "Direct competition from incumbents like Figma, Notion, Slack, and Microsoft Teams",
            "Scaling challenges under high-frequency socket synchronization loads"
        ]
    }

    pitch_deck = [
        {
            "slide_num": 1,
            "title": "The Problem",
            "bullets": [
                "Modern product teams are fragmented across Canva (designs), Notion (documents), and GitHub (code repos).",
                "Context switching is expensive, and data sinks are siloed behind closed proprietary clouds."
            ]
        },
        {
            "slide_num": 2,
            "title": f"The Solution: {title}",
            "bullets": [
                f"A unified open-source operating space that merges text docs, canvas diagrams, and branch controls.",
                "Designed with modular schemas to evolve alongside your codebases."
            ]
        },
        {
            "slide_num": 3,
            "title": "Business Mechanics",
            "bullets": [
                "Open-Core billing: Host it yourself for free or purchase our managed cloud instances.",
                "Ecosystem scale: Plugin developers publish themes and workflow integrations to our marketplace."
            ]
        }
    ]

    roadmap = [
        {"phase": "Phase 1 - Prototype Alpha", "milestones": ["Websocket room broker implementation", "Basic block text editor & canvas UI integration", "Local database persistence schemas"]},
        {"phase": "Phase 2 - Public Beta", "milestones": ["Real-time collaborative YJS hooks integration", "Full developer OpenAPI spec definitions", "Open source replacements recommendations engine"]},
        {"phase": "Phase 3 - Scale & Multi-tenant", "milestones": ["SSO (Keycloak Integration)", "Automated cost calculator monitors", "SaaS production billing release"]}
    ]

    return {
        "pitch_slides": pitch_deck,
        "pricing": pricing,
        "swot": swot,
        "roadmap": roadmap
    }

from typing import Dict, Any, List

def calculate_costs(prompt: str, intent: Dict[str, Any], genomes: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate infrastructure costing matrices and caching optimizations.
    """
    scale = intent["scale"]

    hosting_tiers = [
        {
            "scale": "Development / Small Team (1-10 users)",
            "server": "1x VPS (2 vCPU, 4GB RAM) - $10/mo",
            "database": "SQLite / Local Postgres - $0/mo",
            "storage": "Local Block Storage - $0/mo",
            "total_estimate": "$10 to $20 per month"
        },
        {
            "scale": "Production Scaling (100 - 1000 users)",
            "server": "2x App Nodes (4 vCPU, 8GB RAM) behind load balancer - $80/mo",
            "database": "Managed Postgres (2 vCPU, 4GB RAM, HA) - $60/mo",
            "storage": "S3 (200GB storage + bandwidth) - $15/mo",
            "redis_cache": "Managed Redis cache node - $25/mo",
            "total_estimate": "$180 per month"
        }
    ]

    llm_costs = [
        {
            "operation": "Intent Search Embedding Vectorizing",
            "model": "SentenceTransformers (local) or text-embedding-ada-002",
            "unit_cost": "Free (local) or $0.0001 per 1K tokens",
            "monthly_run": "$0.50 (low volume)"
        },
        {
            "operation": "Co-pilot Text Summarization & Revision generation",
            "model": "gpt-4o-mini / Claude 3 Haiku",
            "unit_cost": "$0.00015 input / $0.0006 output per 1K tokens",
            "monthly_run": "$45.00 (avg 500 prompts per user daily)"
        }
    ]

    optimizations = [
        "1. Cache workspace layout files and active page nodes using Redis to prevent database querying spikes.",
        "2. Compress WebSocket sync packets (using binary Protobuf / YJS vectors) to reduce monthly egress bandwidth costs by up to 60%.",
        "3. Route non-critical LLM generation queries to local on-premise Ollama instances to reduce API bills to zero."
    ]

    return {
        "hosting_tiers": hosting_tiers,
        "llm_costs": llm_costs,
        "optimizations": optimizations
    }

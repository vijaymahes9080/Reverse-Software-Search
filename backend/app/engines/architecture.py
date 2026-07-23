from typing import Dict, Any, List
from app.services.llm_service import call_llm

def generate_architecture(prompt: str, intent: Dict[str, Any], genomes: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate service components, architecture diagram and configuration rules.
    """
    title = intent["title"]
    
    # Simple diagram definitions that look amazing in mermaid
    mermaid_diagram = f"""graph TD
    %% Styling
    classDef client fill:#0ea5e9,stroke:#0284c7,stroke-width:2px,color:#fff;
    classDef gateway fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff;
    classDef service fill:#10b981,stroke:#059669,stroke-width:2px,color:#fff;
    classDef queue fill:#f59e0b,stroke:#d97706,stroke-width:2px,color:#fff;
    classDef storage fill:#ef4444,stroke:#dc2626,stroke-width:2px,color:#fff;

    Client["💻 Client (Next.js SPA)"]:::client
    Gateway["🛡️ API Gateway (FastAPI / Traefik)"]:::gateway
    
    subgraph "Core Service Mesh"
        AuthService["🔑 Keycloak Auth Service"]:::service
        AppService["⚙️ {title} API Service"]:::service
        WorkerService["🏗️ Celery Background Workers"]:::service
    end
    
    subgraph "State & Event Store"
        Redis["⚡ Redis Cache & Broker"]:::queue
        DB["📁 PostgreSQL Database"]:::storage
        VectorDB["🔍 Qdrant Vector Store"]:::storage
        S3["📦 MinIO Object Storage"]:::storage
    end

    Client -->|HTTPS / WSS| Gateway
    Gateway -->|Authentication| AuthService
    Gateway -->|REST / WebSockets| AppService
    
    AppService -->|Caching & PubSub| Redis
    AppService -->|Transactions| DB
    AppService -->|Semantic Indexes| VectorDB
    AppService -->|Media Assets| S3
    
    WorkerService -->|Dequeue Tasks| Redis
    WorkerService -->|Update State| DB
    WorkerService -->|Build DNA indexes| VectorDB
    
    class Client,Gateway client;
    class AuthService,AppService,WorkerService service;
    class Redis queue;
    class DB,VectorDB,S3 storage;
"""

    services = [
        {
            "name": f"{title} Frontend API",
            "type": "Next.js & TypeScript Server Side Rendering",
            "responsibility": "Serves user interfaces, manages local state, executes real-time CRDT drawing canvas synchronizations.",
            "tech": "React, TailwindCSS, Zustand, React Flow"
        },
        {
            "name": "FastAPI Core Gateway Engine",
            "type": "Asynchronous REST & WebSocket Backend",
            "responsibility": "Handles client WebSocket routing, parses intent genomes, triggers backend tasks, routes user API access.",
            "tech": "FastAPI, Uvicorn, SQLAlchemy"
        },
        {
            "name": "Asynchronous Event Worker",
            "type": "Distributed Celery Task Service",
            "responsibility": "Handles heavy repository synthesis, file bundling, vectorizing code templates, and static code generation pipelines.",
            "tech": "Celery, Redis, SentenceTransformers"
        }
    ]
    
    decision_reasoning = (
        "1. Hybrid Monorepo approach is selected to keep deployment simple while supporting separation between Next.js client nodes and Python generation microservices.\n"
        "2. Redis acts as both a caching layer for database pages and a celery message broker to prevent heavy codebase compilation loops from blocking the HTTP workers.\n"
        "3. PostgreSQL stores relational tables (users, roles, settings) while Qdrant or SQLite indexes document vector trees for reverse semantic searches."
    )

    return {
        "pattern": "Modular Hybrid Monorepo",
        "mermaid": mermaid_diagram,
        "services": services,
        "reasoning": decision_reasoning
    }

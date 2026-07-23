import os

class Settings:
    PROJECT_NAME: str = "Reverse Software Search"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./rss.db")
    
    # LLM Settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LITELLM_MODEL: str = os.getenv("LITELLM_MODEL", "gpt-4o-mini")  # Default model
    LITELLM_API_BASE: str = os.getenv("LITELLM_API_BASE", "")
    
    # Local fallback/Mock mode
    MOCK_LLM: bool = os.getenv("MOCK_LLM", "True").lower() in ("true", "1", "yes")

    # Vector store setup
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", "6333"))
    USE_QDRANT: bool = False

    # Neo4j Graph Database
    NEO4J_URI: str = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "password")
    USE_NEO4J: bool = False

settings = Settings()

from typing import Dict, Any, List

def design_database(prompt: str, intent: Dict[str, Any], genomes: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate ER layout and database schemas (SQL table creation scripts).
    """
    title = intent["title"].lower().replace(" ", "_")
    
    # Generate schema based on matched genomes
    tables = [
        {
            "name": "workspaces",
            "description": "Represents separate organization tenants or user workspaces.",
            "columns": [
                {"name": "id", "type": "UUID (PK)", "constraints": "NOT NULL"},
                {"name": "name", "type": "VARCHAR(255)", "constraints": "NOT NULL"},
                {"name": "slug", "type": "VARCHAR(255)", "constraints": "UNIQUE, NOT NULL"},
                {"name": "owner_id", "type": "UUID (FK)", "constraints": "REFERENCES users(id)"},
                {"name": "created_at", "type": "TIMESTAMP", "constraints": "DEFAULT NOW()"}
            ]
        },
        {
            "name": "users",
            "description": "User profiles and credentials mappings.",
            "columns": [
                {"name": "id", "type": "UUID (PK)", "constraints": "NOT NULL"},
                {"name": "email", "type": "VARCHAR(255)", "constraints": "UNIQUE, NOT NULL"},
                {"name": "full_name", "type": "VARCHAR(255)", "constraints": ""},
                {"name": "hashed_password", "type": "VARCHAR(255)", "constraints": "NOT NULL"},
                {"name": "is_active", "type": "BOOLEAN", "constraints": "DEFAULT TRUE"}
            ]
        },
        {
            "name": "nodes",
            "description": "Core hierarchical elements (pages, canvases, source repositories, or files).",
            "columns": [
                {"name": "id", "type": "UUID (PK)", "constraints": "NOT NULL"},
                {"name": "workspace_id", "type": "UUID (FK)", "constraints": "REFERENCES workspaces(id) ON DELETE CASCADE"},
                {"name": "parent_id", "type": "UUID (FK)", "constraints": "REFERENCES nodes(id) ON DELETE SET NULL"},
                {"name": "title", "type": "VARCHAR(255)", "constraints": "NOT NULL"},
                {"name": "node_type", "type": "VARCHAR(50)", "constraints": "NOT NULL (e.g. 'document', 'canvas', 'codefile')"},
                {"name": "content", "type": "TEXT", "constraints": "NULL"},
                {"name": "metadata_json", "type": "JSONB", "constraints": "DEFAULT '{}'"},
                {"name": "updated_at", "type": "TIMESTAMP", "constraints": "DEFAULT NOW()"}
            ]
        },
        {
            "name": "node_revisions",
            "description": "Audit trails and historical revisions for collaborative work.",
            "columns": [
                {"name": "id", "type": "UUID (PK)", "constraints": "NOT NULL"},
                {"name": "node_id", "type": "UUID (FK)", "constraints": "REFERENCES nodes(id) ON DELETE CASCADE"},
                {"name": "edited_by", "type": "UUID (FK)", "constraints": "REFERENCES users(id)"},
                {"name": "delta_json", "type": "TEXT", "constraints": "NOT NULL"},
                {"name": "revision_number", "type": "INTEGER", "constraints": "NOT NULL"}
            ]
        }
    ]

    # Generate standard SQL script
    sql_script = ""
    for table in tables:
        sql_script += f"-- Table: {table['name']}\n"
        sql_script += f"CREATE TABLE {table['name']} (\n"
        cols_str = []
        for col in table["columns"]:
            col_def = f"    {col['name']} {col['type']}"
            if col["constraints"]:
                # Strip PK/FK notations for raw SQL compilation
                clean_type = col["type"].split(" (")[0]
                col_def = f"    {col['name']} {clean_type} {col['constraints']}"
            cols_str.append(col_def)
        sql_script += ",\n".join(cols_str)
        sql_script += "\n);\n\n"
        
        # Add index
        sql_script += f"CREATE INDEX idx_{table['name']}_id ON {table['name']}(id);\n"
        if table['name'] == 'nodes':
            sql_script += f"CREATE INDEX idx_{table['name']}_workspace_id ON {table['name']}(workspace_id);\n"
        sql_script += "\n"

    # Create visual ER diagram in Mermaid
    er_diagram = """erDiagram
    users ||--o{ workspaces : owns
    workspaces ||--o{ nodes : contains
    nodes ||--o{ node_revisions : audits
    users ||--o{ node_revisions : creates
    nodes ||--o{ nodes : subfolders
"""

    return {
        "tables": tables,
        "sql": sql_script,
        "er_diagram": er_diagram
    }

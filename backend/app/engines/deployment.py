from typing import Dict, Any, List

def plan_deployment(prompt: str, intent: Dict[str, Any], genomes: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate reverse proxy configs, CDN scaling plans, backup rules, and GitHub actions CI workflows.
    """
    title = intent["title"]

    github_action_ci = """name: System CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r backend/requirements.txt
          pip install pytest
      - name: Run Backend Tests
        run: pytest backend

  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install dependencies
        run: |
          cd frontend
          npm install
      - name: Run Frontend Build
        run: |
          cd frontend
          npm run build
"""

    nginx_config = f"""server {{
    listen 80;
    server_name local.{title.lower().replace(" ", "")}.com;

    location / {{
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }}

    location /api/v1/ {{
        proxy_pass http://localhost:8000/api/v1/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }}

    location /ws/ {{
        proxy_pass http://localhost:8000/ws/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }}
}}
"""

    return {
        "nginx_reverse_proxy": nginx_config,
        "ci_cd_workflow": github_action_ci,
        "monitoring": {
            "logging": "OpenTelemetry with Grafana / Loki collector",
            "metrics": "Prometheus exporter mapping WebSocket connection counts",
            "tracing": "Jaeger context spans routing across services"
        },
        "disaster_recovery": "Nightly compressed DB dumps saved to MinIO/S3 buckets with 30-day retention policies."
    }

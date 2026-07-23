# 🔍 Reverse Software Search (RSS)

> **Translate natural language product concepts into complete engineering blueprints, capabilities graphs, database designs, architecture diagrams, and download-ready starter repositories.**

Reverse Software Search (RSS) is an AI-powered software synthesis engine. By entering high-level, hybrid prompts (such as *"I want Discord for hospitals"* or *"I want Notion but offline"*), RSS reverse-engineers the "genetic components" of leading software platforms, synthesizes custom engineering specifications across 17 distinct design dimensions, and produces a complete, deployable boilerplate package ready for download.

---

## ✨ Features & Capabilities

RSS leverages a modular multi-engine pipeline to generate a comprehensive architectural blueprint:

1. **Software Genome Matching**: Maps your prompt against pre-seeded profiles of industry giants (**Notion**, **GitHub**, **Canva**, **Discord**, **Slack**, **VSCode**) to copy their structural patterns, tech stacks, and schemas.
2. **Dynamic Capability Graphs**: Uses `NetworkX` on the backend and `@xyflow/react` (React Flow) on the frontend to render interactive service meshes, data flows, and module dependencies.
3. **Database Designer**: Synthesizes custom entity-relationship attributes and outputs complete PostgreSQL/SQLite DDL schemas.
4. **API Specification Generator**: Generates clean, RESTful OpenAPI/Swagger endpoints and WebSocket routes.
5. **Interactive UI Layouts**: Maps client routes, core layouts, and custom UI elements.
6. **User Journey & Workflows**: Generates sequence diagrams and user interaction maps.
7. **Infrastructure & LLM Cost Calculator**: Estimates monthly AWS/GCP cloud hosting and LLM token costs.
8. **OSS Replacement Recommendations**: Recommends open-source, self-hosted alternatives to replace proprietary elements.
9. **Startup Generator**: Produces complete pricing tiers, Go-To-Market (GTM) strategies, SWOT analysis, and pitch deck structures.
10. **Codebase Repository Synthesizer**: Compiles and outputs complete Next.js, FastAPI, Docker, and environment files in real-time, packaged inside a downloadable `.zip` archive.

---

## 🛠️ Technology Stack

### Backend
* **Core Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.10+)
* **Database / ORM**: SQLite (development default) / PostgreSQL, managed via [SQLAlchemy](https://www.sqlalchemy.org/)
* **AI Orchestration**: [LiteLLM](https://github.com/BerriAI/litellm) for uniform API calls to OpenAI, Claude, and local LLMs
* **Graph Modeling**: [NetworkX](https://networkx.org/) for capability graph layouts and topological queries
* **Code Generation**: [Jinja2](https://jinja.palletsprojects.com/) template compilation

### Frontend
* **Core Framework**: [Next.js 16](https://nextjs.org/) (App Router), [React 19](https://react.dev/), [TypeScript](https://www.typescriptlang.org/)
* **Graph Visualization**: [@xyflow/react](https://reactflow.dev/) (React Flow) for highly custom, interactive node layouts
* **Styling**: TailwindCSS 4 (via `@tailwindcss/postcss`) and vanilla CSS variables
* **Animations**: [Framer Motion](https://www.framer.com/motion/) for premium micro-interactions and transitions
* **State Management**: [Zustand](https://github.com/pmndrs/zustand)
* **Icons**: [Lucide React](https://lucide.dev/)
* **Visual Effects**: [canvas-confetti](https://github.com/catdad/canvas-confetti) for success highlights

---

## 📂 Project Structure

```
Reverse Software Search/
├── backend/
│   ├── app/
│   │   ├── engines/               # The 17 software synthesis sub-engines
│   │   │   ├── ai_planner.py      # Plans AI prompt chains and model routing
│   │   │   ├── api_generator.py   # Generates OpenAPI REST & WebSockets specs
│   │   │   ├── architecture.py    # Service mesh and system design planner
│   │   │   ├── cost_analyzer.py   # Cloud infrastructure & token cost calculator
│   │   │   ├── db_designer.py     # Generates schemas, tables, and SQL DDLs
│   │   │   ├── deployment.py      # Builds Dockerfiles, Compose, and K8s manifests
│   │   │   ├── genome_matcher.py  # Computes software genome similarity matches
│   │   │   ├── innovation.py      # Analyzes product market gaps and innovation vectors
│   │   │   ├── intent.py          # Extracted product audience, constraints, scope
│   │   │   ├── oss.py             # Maps components to open-source alternatives
│   │   │   ├── repo_generator.py  # Generates boilerplate code structure
│   │   │   ├── startup.py         # Startup blueprints (SWOT, pricing, GTM)
│   │   │   └── synthesis_pipeline.py # Main pipeline orchestrating all engines
│   │   ├── models/                # SQLAlchemy database models
│   │   ├── services/              # Shared data and business utilities
│   │   │   ├── capability_graph.py# In-memory system capability list & NetworkX graph
│   │   │   ├── genome_data.py     # Pre-seeded software genome specifications
│   │   │   └── llm_service.py     # LiteLLM connection setup
│   │   ├── config.py              # Environment configuration & defaults
│   │   ├── database.py            # SQLite session connections
│   │   └── main.py                # FastAPI routes, endpoints, CORS rules, & zip exporter
│   ├── requirements.txt           # Python backend dependencies
│   └── rss.db                     # Local SQLite database storing history
│
├── frontend/
│   ├── src/
│   │   ├── app/                   # Next.js app pages, styles, layout
│   │   │   ├── globals.css        # Main Tailwind configuration and custom styling
│   │   │   ├── layout.tsx         # Global page template
│   │   │   └── page.tsx           # Comprehensive RSS interactive UI dashboard
│   │   └── components/            # Custom UI elements
│   │       ├── ArchitectureGraph.tsx # React Flow capability canvas renderer
│   │       └── CodePreview.tsx    # Visual file explorer & editor previewer
│   ├── package.json               # Node.js dependencies
│   └── tsconfig.json              # TypeScript compilation setup
└── README.md                      # Project documentation (this file)
```

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.10+**
* **Node.js 18+**

---

### 1. Setting Up the Backend API

1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

   # On Windows (PowerShell):
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (Optional):
   Create a `.env` file or export variables:
   ```env
   OPENAI_API_KEY=your-openai-api-key   # Optional if running in Mock Mode
   LITELLM_MODEL=gpt-4o-mini
   MOCK_LLM=True                        # Set to False to enable live LLM synthesis
   ```
   > 💡 **Mock Mode**: By default, `MOCK_LLM=True` is enabled, allowing you to synthesize blueprints instantly offline for common queries like *"I want Canva + GitHub + Notion"*, *"I want Discord for hospitals"*, *"I want GitHub for lawyers"*, and *"I want Notion but offline"*.

5. Start the FastAPI development server:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   * **Swagger Docs**: Head to [http://localhost:8000/docs](http://localhost:8000/docs) to view and test backend endpoints.

---

### 2. Setting Up the Frontend Client

1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Install Node dependencies:
   ```bash
   npm install
   ```

3. Start the Next.js dev server:
   ```bash
   npm run dev
   ```

4. Access the web app:
   Open [http://localhost:3000](http://localhost:3000) in your web browser.

---

## 🛡️ Database & Persistent Blueprints

When a product concept is synthesized:
1. The app serializes the complex nested schemas generated by all 17 engines into JSON strings.
2. It saves the blueprint metadata and full JSON specifications to the local SQLite database (`backend/rss.db`).
3. The left sidebar displays a **Synthesized History** panel showing previous generation runs, enabling you to reload and inspect past designs without calling the LLM again.

---

## 📦 Zip Archiving & Code Export

The **Code Preview** tab allows you to inspect the boilerplate files (including layout pages, config settings, Docker configurations, and API controllers) synthesized specifically for your app.
* Pressing the **Download Starter Repository** button on the UI requests a generated `.zip` archive compiled in memory on the backend by `repo_generator.py` and streams it directly to your browser for immediate download.

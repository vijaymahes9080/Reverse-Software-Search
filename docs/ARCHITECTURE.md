# Reverse Software Search - System Architecture Specification

## 🏗️ System Overview

Reverse Software Search (RSS) is structured around an 18-engine synthesis pipeline that converts natural language product concepts into production-grade software specifications and starter repositories.

```
[ Natural Language Prompt ]
            │
            ▼
┌───────────────────────┐
│ 1. Intent Extraction  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ 2. Genome Matching    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐      ┌──────────────────────────┐
│ 3. Capability Graph   ├─────►│ 4-15. Sub-Engines        │
└───────────┬───────────┘      │ (DB, API, UI, Costs)     │
            │                  └────────────┬─────────────┘
            ▼                               │
┌───────────────────────┐                   │
│ 16. Multi-Agent Review│◄──────────────────┘
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ 17. Repo Synthesizer  │
└───────────────────────┘
```

## 🧬 Core Components

1. **Intent Extraction Engine**: Parses target audience, technical scale, regulatory constraints, and pricing models.
2. **Capability Graph Engine**: Built using `NetworkX` graph structures to model dependencies between microservices.
3. **Multi-Agent Review Board**: Runs simulated architectural reviews across 4 personas (Principal Architect, FinOps Specialist, Security Officer, UX Strategist).
4. **Codebase Generator**: Assembles Next.js, FastAPI, SQL DDL, and Docker files in real-time.

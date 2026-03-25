# MiroFish Docker Setup

## Prerequisites
- Docker Desktop installed and running
- `.env` file in project root with:
  ```
  LLM_API_KEY=your_key_here
  LLM_BASE_URL=http://host.docker.internal:4000/v1
  LLM_MODEL_NAME=anthropic/claude-haiku-4-5-20251001
  ZEP_API_KEY=your_zep_key_here
  ```

> **Note:** If your LLM proxy runs on localhost, use `host.docker.internal` instead of `localhost` in `LLM_BASE_URL` so the container can reach it.

## Quick Start

```bash
docker compose up
```

That's it. This builds the image (first time takes ~5 min) and starts both services:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5001

## Transferring a Pre-built Image

If you have a pre-built image from another machine:

```bash
# On source machine — export
docker save mirofish:local | gzip > mirofish.tar.gz

# On target machine — import
docker load < mirofish.tar.gz
docker compose up
```

## What's Included

The container runs both frontend (Vite dev server) and backend (Flask) with:
- Python 3.11 + all backend dependencies (Flask, OpenAI, Zep Cloud, CAMEL-OASIS)
- Node.js + frontend dependencies (Vue 3 + Vite)
- PDF report generation (pandoc + weasyprint)
- All local code fixes (PascalCase entity names, SCREAMING_SNAKE_CASE edges, 8192 token ontology limit)

## Running a Simulation (API)

If you can't use the drag-and-drop UI, run the full pipeline via curl:

```bash
# 1. Upload seed file + generate ontology
curl -X POST http://localhost:5001/api/graph/ontology/generate \
  -F "files=@your_context.md" \
  -F "simulation_requirement=Your simulation description here" \
  -F "project_name=My Project"

# 2. Build graph (use project_id from step 1)
curl -X POST http://localhost:5001/api/graph/build \
  -H "Content-Type: application/json" \
  -d '{"project_id": "proj_xxx"}'

# 3. Check graph build progress
curl http://localhost:5001/api/graph/task/{task_id}

# 4. Create simulation
curl -X POST http://localhost:5001/api/simulation/create \
  -H "Content-Type: application/json" \
  -d '{"project_id": "proj_xxx"}'

# 5. Prepare simulation (generates agent profiles + config)
curl -X POST http://localhost:5001/api/simulation/prepare \
  -H "Content-Type: application/json" \
  -d '{"simulation_id": "sim_xxx"}'

# 6. Check preparation status
curl -X POST http://localhost:5001/api/simulation/prepare/status \
  -H "Content-Type: application/json" \
  -d '{"simulation_id": "sim_xxx", "task_id": "task_xxx"}'

# 7. Start simulation
curl -X POST http://localhost:5001/api/simulation/start \
  -H "Content-Type: application/json" \
  -d '{"simulation_id": "sim_xxx", "platform": "parallel", "enable_graph_memory_update": true}'

# 8. Check run status
curl http://localhost:5001/api/simulation/sim_xxx/run-status

# 9. Stop simulation
curl -X POST http://localhost:5001/api/simulation/stop \
  -H "Content-Type: application/json" \
  -d '{"simulation_id": "sim_xxx"}'

# 10. Generate report
curl -X POST http://localhost:5001/api/report/generate \
  -H "Content-Type: application/json" \
  -d '{"simulation_id": "sim_xxx"}'
```

## Stopping

```bash
docker compose down
```

## Rebuilding After Code Changes

```bash
docker compose build
docker compose up
```

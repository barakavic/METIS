# METIS

Modular Extensible Tank Intelligence System (METIS) is a simulation-first platform for real-time water storage feedback, forecasting, and policy-driven recommendations.

## Current Stage

The project is in Phase 1 (simulation mode).

- No live hardware integration yet.
- Core focus is simulation, prediction, and API interfaces.
- Hardware adapters are planned for later phases.

## Planned Architecture

- `domain/`: core models, physics equations, and policy logic.
- `simulation/`: inflow, demand, prediction, and tick engine.
- `infrastructure/`: persistence, repositories, deterministic utilities.
- `api/`: REST and WebSocket endpoints.
- `adapters/`: future hardware abstraction interfaces.

## Quick Start

1. Create and activate a virtual environment.
2. Install project dependencies.
3. Start the API service.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn metis.main:app --reload
```

## Environment Variables

Copy `.env.example` values into your local environment (or a `.env` file if your runner supports it):

- `METIS_ENV`
- `METIS_HOST`
- `METIS_PORT`
- `METIS_LOG_LEVEL`
- `METIS_DB_URL`
- `METIS_SIM_TICK_SECONDS`
- `METIS_FORECAST_EVERY_TICKS`
- `METIS_RANDOM_SEED`

## Initial Health Check

After starting the service:

- `GET /health` returns app health status.
- `GET /` returns a minimal API banner.

## Roadmap

Execution plan is maintained in `Docs/roadplan.md`.

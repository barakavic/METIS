from fastapi import FastAPI

from metis.config import settings

app = FastAPI(
    title='METIS API',
    version='0.1.0',
    description='Simulation-first water storage intelligence platform.',
)


@app.get('/')
def root() -> dict[str, str]:
    return {
        'service': 'METIS',
        'mode': settings.metis_env,
        'status': 'running',
    }


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}

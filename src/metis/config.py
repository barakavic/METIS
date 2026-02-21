from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    metis_env: str = Field(default='development', alias='METIS_ENV')
    metis_host: str = Field(default='127.0.0.1', alias='METIS_HOST')
    metis_port: int = Field(default=8000, alias='METIS_PORT')
    metis_log_level: str = Field(default='INFO', alias='METIS_LOG_LEVEL')
    metis_db_url: str = Field(default='sqlite:///./metis.db', alias='METIS_DB_URL')
    metis_sim_tick_seconds: int = Field(default=1, alias='METIS_SIM_TICK_SECONDS')
    metis_forecast_every_ticks: int = Field(default=5, alias='METIS_FORECAST_EVERY_TICKS')
    metis_random_seed: int = Field(default=42, alias='METIS_RANDOM_SEED')


settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    APP_NAME: str = "zuplae-python-starter"
    APP_DESCRIPTION: str = "Boilerplate"
    APP_VERSION: str = "0.0.1"

    API_PREFIX_V1: str = "/api/v1"

    API_CORS_ORIGINS: List[str] = ["*"]

    LOG_LEVEL: str = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    ENABLE_UVICORN_ACCESS_LOGS: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

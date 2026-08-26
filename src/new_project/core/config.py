from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Core application settings managed by Pydantic.
    Reads from environment variables and a local .env file.
    """

    # Configure Pydantic to read from a .env file if it exists,
    # ignoring any extra variables it doesn't recognize.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Core Settings
    environment: Literal["development", "staging", "production"] = "development"
    default_log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached instance of the settings so we don't re-read
    the environment/files on every call.
    """
    return Settings()

import logging
import sys
from typing import Tuple
from functools import lru_cache
from loguru import logger

from pydantic import BaseSettings

from core.logging import InterceptHandler


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    app_name: str = "music_spotify_microservice"
    redis_url: str

    SPOTYFI_CLIENT_ID: str
    SPOTYFI_SECRET_KEY: str

    proxy_url: str

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        env_file = ".env"

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])

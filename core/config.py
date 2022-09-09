from pydantic import BaseSettings
from functools import lru_cache


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    app_name: str = "music_spotify_microservice"
    redis_url: str

    SPOTYFI_CLIENT_ID: str
    SPOTYFI_SECRET_KEY: str

    proxy_url: str

    class Config:
        env_file = ".env"

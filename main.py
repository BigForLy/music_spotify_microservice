from fastapi import FastAPI
from api.routes import router as router_api
from core.config import get_settings


def get_application() -> FastAPI:
    settings = get_settings()

    settings.configure_logging()

    application = FastAPI()
    application.include_router(router_api, prefix="/api")

    return application


app = get_application()

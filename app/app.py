from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import router as v1_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import setup_logging, get_logger


class Application(FastAPI):
    def __init__(self):
        setup_logging()
        super().__init__(
            title=settings.APP_NAME,
            description=settings.APP_DESCRIPTION,
            version=settings.APP_VERSION,
        )
        self.add_middleware(
            CORSMiddleware,
            allow_origins=settings.API_CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        # routes
        self.include_router(v1_router, prefix=settings.API_PREFIX_V1)

        logger = get_logger(__name__)
        logger.info("Application started", extra={"service": settings.APP_NAME})

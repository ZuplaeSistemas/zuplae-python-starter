from __future__ import annotations

import logging
from logging.config import dictConfig

from app.core.config import settings


def setup_logging() -> None:
    """
    Configura logging para a aplicação + uvicorn (error/access).
    Lê nível e flags do settings (pydantic-settings).
    """
    level = (settings.LOG_LEVEL or "INFO").upper()
    access_level = "INFO" if settings.ENABLE_UVICORN_ACCESS_LOGS else "WARNING"

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
                # Formatter específico do uvicorn.access (tem campos extras)
                "access": {
                    "format": "%(asctime)s - %(levelname)s - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": level,
                    "stream": "ext://sys.stdout",
                },
                "access_console": {
                    "class": "logging.StreamHandler",
                    "formatter": "access",
                    "level": access_level,
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {
                # Seus logs de app: use get_logger(__name__)
                "app": {
                    "handlers": ["console"],
                    "level": level,
                    "propagate": False,
                },
                # Uvicorn core/error
                "uvicorn": {
                    "handlers": ["console"],
                    "level": level,
                    "propagate": False,
                },
                "uvicorn.error": {
                    "handlers": ["console"],
                    "level": level,
                    "propagate": False,
                },
                # Access log (requests HTTP)
                "uvicorn.access": {
                    "handlers": ["access_console"],
                    "level": access_level,
                    "propagate": False,
                },
            },
            # Root logger: útil para libs que não têm logger dedicado
            "root": {
                "handlers": ["console"],
                "level": level,
            },
        }
    )


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Retorna um logger padronizado (use `get_logger(__name__)` nos módulos).
    """
    return logging.getLogger(name or "app")

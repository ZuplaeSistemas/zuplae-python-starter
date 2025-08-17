from typing import Annotated
from fastapi import Depends

from app.domains.health.repository import HealthRepository, InMemoryHealthRepository
from app.domains.health.use_case import HealthUseCase


def get_health_repo() -> HealthRepository:
    # No futuro: trocar por um repo que checa conexões externas (DB, S3, etc.)
    return InMemoryHealthRepository()


def get_check_health(
    repo: Annotated[HealthRepository, Depends(get_health_repo)],
) -> HealthUseCase:
    return HealthUseCase(repo)

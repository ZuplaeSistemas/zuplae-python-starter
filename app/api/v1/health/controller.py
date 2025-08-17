from fastapi import APIRouter, Depends
from app.api.v1.health.schema import HealthResponse
from app.domains.health.use_case import HealthUseCase
from app.core.deps import get_check_health
from app.core.logging import get_logger


router = APIRouter(prefix="/health", tags=["health"])

logger = get_logger(__name__)


@router.get("/liveness", response_model=HealthResponse)
def liveness() -> HealthResponse:
    logger.info("get liveness")
    return HealthResponse(status="ok", service="zuplae-python-starter")


@router.get("/readiness", response_model=HealthResponse)
def readiness(check: HealthUseCase = Depends(get_check_health)) -> HealthResponse:
    # Está pronto = dependências essenciais OK.
    logger.info("get readiness")
    ok = check.execute()
    return HealthResponse(
        status="ok" if ok else "degraded", service="zuplae-python-starter"
    )

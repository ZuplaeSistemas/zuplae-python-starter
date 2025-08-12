from fastapi import APIRouter
from app.api.v1.health.controller import router as health_router

router = APIRouter()
router.include_router(health_router)
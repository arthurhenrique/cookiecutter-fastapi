from fastapi import APIRouter

from api.routes import predictor

router = APIRouter()
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
router.include_router(predictor.router, tags=["health"], prefix="/v1")

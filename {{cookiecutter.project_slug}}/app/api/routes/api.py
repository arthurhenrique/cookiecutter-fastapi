from fastapi import APIRouter

from app.api.routes import sample, predictor

router = APIRouter()
router.include_router(sample.router, tags=["sample"], prefix="/v1")
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")

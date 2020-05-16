from fastapi import APIRouter

from app.api.routes import predictor

router = APIRouter()
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")

from fastapi import APIRouter

from api.routes import predictor

router = APIRouter()
router.include_router(sapredictorple.router, tags=["predictor"], prefix="/v1")

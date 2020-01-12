from fastapi import APIRouter

from app.api.routes import sample

router = APIRouter()
router.include_router(sample.router, tags=["sample"], prefix="/v1")

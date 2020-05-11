from fastapi import APIRouter

from app.services.predict import MachineLearningModelHandlerScore
from app.models.prediction import MachineLearningResponse
from typing import Any

router = APIRouter()


@router.get("/predict", response_model=MachineLearningResponse, name="predict:get-data")
async def predict(data_input: Any = None):
    scoring = MachineLearningModelHandlerScore()
    return MachineLearningResponse(score=scoring.predict(data_input))

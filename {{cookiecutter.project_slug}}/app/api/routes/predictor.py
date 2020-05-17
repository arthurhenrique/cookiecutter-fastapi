from typing import Any

import joblib
from fastapi import APIRouter, HTTPException
from loguru import logger
from models.prediction import MachineLearningResponse, HealthResponse
from services.predict import MachineLearningModelHandlerScore as model

router = APIRouter()

get_prediction = lambda data_input: MachineLearningResponse(
    model.predict(data_input, load_wrapper=joblib.load, method="predict_proba")
)


@router.get("/predict", response_model=MachineLearningResponse, name="predict:get-data")
async def predict(data_input: Any = None):
    return get_prediction(data_input)


@router.get(
    "/health", response_model=HealthResponse, name="health:get-data",
)
async def health():
    is_health = False
    try:
        get_prediction("lorem ipsum")
        is_health = True
        return HealthResponse(status=is_health)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")

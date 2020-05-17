from typing import Any

import joblib
from fastapi import APIRouter, HTTPException
from loguru import logger
from models.prediction import MachineLearningResponse, HealthResponse
from services.predict import MachineLearningModelHandlerScore as model

router = APIRouter()

# TODO: Change 'load_wrapper' and 'method'  based on your {{cookiecutter.machine_learn_model_name}}.
get_prediction = lambda data_input: MachineLearningResponse(
    model.predict(data_input, load_wrapper=joblib.load, method="predict_proba")
)


@router.get("/predict", response_model=MachineLearningResponse, name="predict:get-data")
async def predict(data_input: Any = None):
    try:
        if not data_input:
            raise HTTPException(
                status_code=404, detail=f"'data_input' argument invalid!"
            )
        prediction = get_prediction(data_input)
        return MachineLearningResponse(prediction=prediction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exception: {e}")


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

from typing import Any

import joblib
from fastapi import APIRouter
from loguru import logger
from models.prediction import MachineLearningResponse
from services.predict import MachineLearningModelHandlerScore as model

router = APIRouter()


@router.get("/predict", response_model=MachineLearningResponse, name="predict:get-data")
async def predict(data_input: Any = None):
    return MachineLearningResponse(
        model.predict(data_input, load_wrapper=joblib.load, method="predict_proba")
    )

from fastapi import APIRouter

from services.predict import MachineLearningModelHandlerScore as model
from models.prediction import MachineLearningResponse
from typing import Any
import joblib
from loguru import logger

router = APIRouter()


@router.get("/predict", response_model=MachineLearningResponse, name="predict:get-data")
async def predict(data_input: Any = None):
    return MachineLearningResponse(
        model.predict(data_input, load_wrapper=joblib.load, method="predict_proba")
    )

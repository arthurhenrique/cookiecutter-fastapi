import json
from pathlib import Path

import joblib
from core.config import INPUT_EXAMPLE
from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool
from models.prediction import (
    HealthResponse,
    MachineLearningDataInput,
    MachineLearningResponse,
)
from services.predict import MachineLearningModelHandlerScore as model

router = APIRouter()


def get_prediction(data_point):
    return model.predict(data_point, load_wrapper=joblib.load, method="predict")


def get_prediction_label(prediction):
    if prediction == 1:
        return "label ok"
    return "label nok"


@router.post(
    "/predict",
    response_model=MachineLearningResponse,
    name="predict:get-data",
)
async def predict(data_input: MachineLearningDataInput):
    if not data_input:
        raise HTTPException(status_code=404, detail="'data_input' argument invalid!")
    try:
        data_point = data_input.get_np_array()
        prediction = await run_in_threadpool(get_prediction, data_point)
        try:
            prediction = float(prediction[0])
        except (TypeError, IndexError, KeyError):
            prediction = float(prediction)
        prediction_label = get_prediction_label(prediction)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}") from err

    return MachineLearningResponse(
        prediction=prediction, prediction_label=prediction_label
    )


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
async def health():
    try:
        content = await run_in_threadpool(Path(INPUT_EXAMPLE).read_text)
        test_input = MachineLearningDataInput(**json.loads(content))
        test_point = test_input.get_np_array()
        await run_in_threadpool(get_prediction, test_point)
        return HealthResponse(status=True)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")

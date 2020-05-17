from pydantic import BaseModel
from typing import Optional


class MachineLearningResponse(BaseModel):
    prediction: float


class HealthResponse(BaseModel):
    status: bool

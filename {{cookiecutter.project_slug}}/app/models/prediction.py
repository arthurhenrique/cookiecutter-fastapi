from pydantic import BaseModel
from typing import Optional


class MachineLearningResponse(BaseModel):
    score: float


class HealthResponse(BaseModel):
    status: bool

import numpy as np
from pydantic import BaseModel


class MachineLearningResponse(BaseModel):
    prediction: float
    prediction_label: str


class HealthResponse(BaseModel):
    status: bool


class MachineLearningDataInput(BaseModel):
    horas_sono: float
    alimentacao_saudavel: float
    nivel_estresse: float
    exercicio: float

    def get_np_array(self):
        return np.array(
            [
                [
                    self.horas_sono,
                    self.alimentacao_saudavel,
                    self.nivel_estresse,
                    self.exercicio,
                ]
            ]
        )

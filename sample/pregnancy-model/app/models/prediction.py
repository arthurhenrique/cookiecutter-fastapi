import numpy as np
from pydantic import BaseModel


class MachineLearningResponse(BaseModel):
    prediction: float
    prediction_label: str


class HealthResponse(BaseModel):
    status: bool


class MachineLearningDataInput(BaseModel):
    idade_mae: float
    horas_sono: float
    alimentacao_saudavel: float
    nivel_estresse: float
    atividade_fisica_semana: float
    renda_familiar: float
    apoio_social: float


    def get_np_array(self):
        return np.array(
            [
                [
                    self.idade_mae,
                    self.horas_sono,
                    self.alimentacao_saudavel,
                    self.nivel_estresse,
                    self.atividade_fisica_semana,
                    self.renda_familiar,
                    self.apoio_social,
                ]
            ]
        )

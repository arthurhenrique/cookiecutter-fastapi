import numpy as np

from pydantic import BaseModel


class MachineLearningResponse(BaseModel):
    prediction: float


class HealthResponse(BaseModel):
    status: bool


class MachineLearningDataInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    feature5: float

    def get_np_array(self):
        return np.array(
            [
                [
                    self.feature1,
                    self.feature2,
                    self.feature3,
                    self.feature4,
                    self.feature5,
                ]
            ]
        )

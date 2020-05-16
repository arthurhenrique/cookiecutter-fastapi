import os

import joblib

from app.core.config import MODEL_NAME, MODEL_PATH
from loguru import logger


class MachineLearningModelHandlerScore(object):
    model = None

    @classmethod
    def get_model(cls):
        if cls.model is None:
            cls.model = cls.load(MODEL_NAME)
        return cls.model

    @classmethod
    def predict(cls, input, method="predict"):
        clf = cls.get_model()
        if hasattr(clf, method):
            return getattr(clf, method)(input)
        raise Exception(f"'{method}' attribute is missing")

    @staticmethod
    def load(file_path: str, load_wrapper_func=joblib.load):
        if MODEL_PATH.endswith("/"):
            path = f"{MODEL_PATH}{file_path}"
        return load_wrapper_func(f"{MODEL_PATH}/{file_path}") or None

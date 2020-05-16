import os

import joblib

from core.config import MODEL_NAME, MODEL_PATH
from loguru import logger


class MachineLearningModelHandlerScore(object):
    model = None

    @classmethod
    def get_model(cls):
        if cls.model is None:
            cls.model = cls.load()
        return cls.model

    @classmethod
    def predict(cls, input, method="predict"):
        clf = cls.get_model()
        if hasattr(clf, method):
            return getattr(clf, method)(input)
        raise Exception(f"'{method}' attribute is missing")

    @staticmethod
    def load(load_wrapper_func=joblib.load):
        model = None
        try:
            if MODEL_PATH.endswith("/"):
                path = f"{MODEL_PATH}{MODEL_NAME}"
            else:
                path = f"{MODEL_PATH}/{MODEL_NAME}"
            if not os.path.exists(path):
                raise FileNotFoundError
            model = load_wrapper_func(path)
        except FileNotFoundError:
            logger.warning(f"Machine learning model at {path} not exists!")
        except Exception as e:
            logger.error(f"{e}!")
        return model

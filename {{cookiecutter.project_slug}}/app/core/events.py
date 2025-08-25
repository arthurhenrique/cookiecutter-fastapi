from typing import Callable

import joblib
from fastapi import FastAPI
from loguru import logger
from sqlalchemy.exc import OperationalError

from core.config import MEMOIZATION_FLAG
from db import Base, engine


def preload_model():
    """
    In order to load model on memory to each worker
    """
    from services.predict import MachineLearningModelHandlerScore

    MachineLearningModelHandlerScore.get_model(joblib.load)


def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        if MEMOIZATION_FLAG:
            preload_model()
        try:
            Base.metadata.create_all(bind=engine)
        except OperationalError:
            logger.exception("failed to initialize database")

    return start_app

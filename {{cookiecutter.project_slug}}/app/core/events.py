from typing import Callable

import requests
from fastapi import FastAPI
from loguru import logger


def preload_model():
    """
    In order to load model on memory to each worker
    """
    from services.predict import MachineLearningModelHandlerScore

    MachineLearningModelHandlerScore.get_model()


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    def start_app() -> None:
        ...

    return start_app

from typing import Callable

import requests

from fastapi import FastAPI
from loguru import logger


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    def start_app() -> None:
        ...

    return start_app

import logging
import sys

from core.logging import InterceptHandler
from loguru import logger
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

API_PREFIX = "/api"
VERSION = "0.1.0"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="")
MEMOIZATION_FLAG: bool = config("MEMOIZATION_FLAG", cast=bool, default=True)

PROJECT_NAME: str = config("PROJECT_NAME", default="manu")

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])

MODEL_PATH = config(
    "MODEL_PATH", default="/Users/arthur.dasilva/repos/arthurhenrique/n"
)
MODEL_NAME = config("MODEL_NAME", default="pregnancy_model_local.joblib")
INPUT_EXAMPLE = config("INPUT_EXAMPLE", default="./ml/model/examples/example.json")

import logging
import sys
from typing import List, Optional

from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from app.core.logging import InterceptHandler
from app.models.pydantic.database import DatabaseURL

config = Config()

VERSION = '0.0.1'

SENTRY_DSN: str = config('SENTRY_DSN', default=None)
DEBUG: bool = config("DEBUG", cast=bool, default=False)

MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

PROJECT_NAME: str = "Book Graphics"
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])

DATABASE: str = config("POSTGRES_DB", cast=str)
DB_USER: Optional[str] = config("POSTGRES_USER", cast=str, default=None)
DB_PASSWORD: Optional[Secret] = config(
    "POSTGRES_PASSWORD", cast=Secret, default=None
)
DB_HOST: str = config("POSTGRES_HOST", cast=str, default="localhost")
DB_PORT: int = config("POSTGRES_PORT", cast=int, default=5432)

DATABASE_CONFIG: DatabaseURL = DatabaseURL(
    drivername="asyncpg",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DATABASE,
)
ALEMBIC_CONFIG: DatabaseURL = DatabaseURL(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DATABASE,
)

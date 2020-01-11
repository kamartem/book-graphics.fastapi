import asyncpg
from fastapi import FastAPI
from loguru import logger

from app.core.config import DATABASE_CONFIG, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {0}", repr(DATABASE_CONFIG.url))

    app.state.pool = await asyncpg.create_pool(
        str(DATABASE_CONFIG.url),
        min_size=MIN_CONNECTIONS_COUNT,
        max_size=MAX_CONNECTIONS_COUNT,
    )

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await app.state.pool.close()

    logger.info("Connection closed")

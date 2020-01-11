from fastapi import FastAPI
from gino.ext.starlette import Gino
from sqlalchemy.schema import MetaData

from app.core.config import DATABASE_CONFIG, DEBUG, PROJECT_NAME, VERSION

application: FastAPI = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
db: MetaData = Gino(application, dsn=DATABASE_CONFIG.url)

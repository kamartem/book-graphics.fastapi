from fastapi.exceptions import RequestValidationError
from sentry_sdk import init as initialize_sentry
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from starlette.exceptions import HTTPException

from app.application import application
from app.core.config import SENTRY_DSN
from app.core.errors.http_error import http_error_handler
from app.core.errors.validation_error import http422_error_handler
from app.core.events.app import create_start_app_handler, create_stop_app_handler
from app.routes.api import router as api_router


def configure():
    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix='/api')

    if SENTRY_DSN not in (None, "", " "):
        initialize_sentry(dsn=SENTRY_DSN, integrations=[SqlalchemyIntegration()])
        application.add_middleware(SentryAsgiMiddleware)


configure()

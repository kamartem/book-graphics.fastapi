ARG PYTHON_VERSION=3.8.1
ARG BUILD_IMAGE=python:${PYTHON_VERSION}-buster
ARG DIST_IMAGE=python:${PYTHON_VERSION}-buster

FROM ${BUILD_IMAGE} as builder

ARG APP_STAGE=prod

COPY ./requirements/ /wheels/requirements/

RUN pip install -U pip && pip wheel -r "/wheels/requirements/${APP_STAGE}.txt"

FROM ${DIST_IMAGE}

ARG APP_DIR=/opt/app
ARG APP_STAGE=prod

COPY --from=builder /wheels /wheels

RUN pip install -U pip \
       && pip install -r "/wheels/requirements/${APP_STAGE}.txt" \
                      -f /wheels \
       && rm -rf /wheels \
       && rm -rf /root/.cache/pip/*

COPY ./docker/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./alembic.ini "${APP_DIR}/"
COPY ./gunicorn.py "${APP_DIR}/"
COPY ./app/ "${APP_DIR}/app/"

WORKDIR "${APP_DIR}"
ENV PYTHONPATH="${APP_DIR}"
EXPOSE 80

ENTRYPOINT [ "/entrypoint" ]

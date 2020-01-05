ARG PYTHON_VERSION=3.8.1
ARG BUILD_IMAGE=python:${PYTHON_VERSION}-buster
ARG DIST_IMAGE=python:${PYTHON_VERSION}-buster

FROM ${BUILD_IMAGE} as builder

ARG APP_STAGE=prod

COPY ./backend/requirements/ /wheels/requirements/

RUN pip install -U pip && pip wheel -r "/wheels/requirements/${APP_STAGE}.txt"

FROM ${DIST_IMAGE}

ARG APP_DIR=/opt/app
ARG APP_STAGE=prod

COPY --from=builder /wheels /wheels
RUN ls -la /wheels/
RUN ls -la /wheels/requirements
RUN ls -la "/wheels/requirements/${APP_STAGE}.txt"
RUN pip install -U pip \
       && pip install -r "/wheels/requirements/${APP_STAGE}.txt" \
                      -f /wheels \
       && rm -rf /wheels \
       && rm -rf /root/.cache/pip/*

COPY ./_docker/backend/entrypoint /entrypoint
RUN chmod +x /entrypoint
COPY ./backend/ "${APP_DIR}/"

WORKDIR "${APP_DIR}/src"
ENV PYTHONPATH="${APP_DIR}/src"
EXPOSE 80

ENTRYPOINT [ "/entrypoint" ]

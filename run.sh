#!/bin/bash

# Available parameters are:
# --service-name <service-name> - starts specific service with its dependencies
# --down - stops and removes containers of running services
# --logs - displays logs output for all services or only for service specified by '--service-name' parameter
# --pull - pulls fresh images before starting containers

set -ea

[ -f .env.sample ] && source .env.sample
[ -f .env ] && source .env

UNKNOWN_POSITIONAL_PARAMS=()

while [ "$#" -gt 0 ]; do
    key="$1"

    case $key in
        --service-name)
            SERVICE_NAME="$2"
            shift # past parameter
            shift # past value

            if [ -z "${SERVICE_NAME-false}" ]; then
                printf '%s\n' "Value for '--service-name' parameter is required!"
                exit 1
            fi
            ;;
        --down)
            DOWN="$1"
            shift # past parameter
            ;;
        --push)
            PUSH="$1"
            shift # past parameter
            ;;
        --logs)
            LOGS="$1"
            shift # past parameter
            ;;
        --pull)
            PULL="$1"
            shift # past parameter
            ;;
        *)    # unknown option
            UNKNOWN_POSITIONAL_PARAMS+=("$1")
            shift # past parameter
            ;;
    esac
done

if [ "${#UNKNOWN_POSITIONAL_PARAMS[@]}" -ne 0 ]; then
    printf '%s\n' "Unrecognized parameters: '${UNKNOWN_POSITIONAL_PARAMS[*]}'"
    printf '%s\n' "Available parameters are:"
    printf '%s\n' "--service-name <service-name> - specifies service that should be started or for which logs should be displayed"
    printf '%s\n' "--down - stops and removes containers of running services"
    printf '%s\n' "--logs - displays logs output for all services or only for service specified by '--service-name' parameter"
    printf '%s\n' "--pull - pulls fresh images before starting containers"

    exit 0
fi

DOCKER_COMPOSE_CONFIG="docker-compose -f docker-compose.yml"
DOCKER_COMPOSE_UP_OPTIONS=""

APP_STAGE=${APP_STAGE:-prod}

printf '%s\n' "Start mode: ${APP_STAGE}"

STAGE_YML="${APP_STAGE}.yml"
if test -f "$STAGE_YML"; then
    DOCKER_COMPOSE_CONFIG+=" -f ${STAGE_YML}"
else
    echo "$STAGE_YML does not exist"
    exit 0
fi

case ${APP_STAGE} in
    local)

        DOCKER_COMPOSE_UP_OPTIONS="--build --force-recreate"
        ;;
    dev)
        DOCKER_COMPOSE_UP_OPTIONS="--build --force-recreate"
        ;;
    stage)
        DOCKER_COMPOSE_UP_OPTIONS="--force-recreate -d"
        ;;
    prod | *)
        DOCKER_COMPOSE_UP_OPTIONS="--force-recreate -d"
        ;;
esac

DOCKER_COMPOSE_DOWN=("${DOCKER_COMPOSE_CONFIG}" "down --remove-orphans")

if [ "${DOWN}" == "--down" ]; then
    printf '%s\n' "Stopping containers, removing containers and networks ..."
    printf '%s\n' "Running command: ${DOCKER_COMPOSE_DOWN[*]}"

    eval "${DOCKER_COMPOSE_DOWN[@]}"

    exit 0;
fi

DOCKER_COMPOSE_LOGS=("${DOCKER_COMPOSE_CONFIG}" "logs --no-color" "${SERVICE_NAME}")

if [ "${LOGS}" == "--logs" ]; then
    printf '%s\n' "Displaying logs output ..."
    printf '%s\n' "Running command: ${DOCKER_COMPOSE_LOGS[*]}"

    eval "${DOCKER_COMPOSE_LOGS[@]}"

    exit 0;
fi

DOCKER_COMPOSE_PUSH=("${DOCKER_COMPOSE_CONFIG}" "push")

if [ "${PUSH}" == "--push" ]; then
    printf '%s\n' "Enforced push of fresh images ..."

    eval "${DOCKER_COMPOSE_PUSH[@]}"

    exit 0;
fi

DOCKER_COMPOSE_UP=("${DOCKER_COMPOSE_CONFIG}" "up" "${DOCKER_COMPOSE_UP_OPTIONS}")

DOCKER_COMPOSE=(
    "${DOCKER_COMPOSE_DOWN[@]}" "&&"
    "${DOCKER_COMPOSE_UP[@]}"
)

DOCKER_COMPOSE_PULL=("${DOCKER_COMPOSE_CONFIG}" "pull --ignore-pull-failures")

if [ "${PULL}" == "--pull" ]; then
    printf '%s\n' "Enforced pull of fresh images ..."

    DOCKER_COMPOSE=("${DOCKER_COMPOSE[@]:0:3}" "${DOCKER_COMPOSE_PULL[@]}" "&&" "${DOCKER_COMPOSE[@]:3}")
fi

if [ "${SERVICE_NAME:=false}" != "false" ]; then
    printf '%s\n' "Starting service: ${SERVICE_NAME} ..."

    DOCKER_COMPOSE=("${DOCKER_COMPOSE[@]}" "${SERVICE_NAME}")
else
    printf '%s\n' "Starting all services ..."
fi

printf '%s\n' "Running command: ${DOCKER_COMPOSE[*]}"

eval "${DOCKER_COMPOSE[@]}"

set +a

FROM node:13.5-buster as builder

ARG APP_DIR=/opt/app
ENV PATH "$APP_DIR/node_modules/.bin":$PATH

WORKDIR $APP_DIR

COPY ./src/ ./

RUN npm ci
RUN npm run build

FROM nginx:1.17.6-alpine
ARG APP_DIR=/opt/app

ADD "./docker/nginx.conf" /etc/nginx/conf.d/default.conf
COPY --from=builder "${APP_DIR}/dist" /usr/share/nginx/html
RUN chown nginx.nginx /usr/share/nginx/html/ -R

EXPOSE 80

ENTRYPOINT ["nginx","-g","daemon off;"]

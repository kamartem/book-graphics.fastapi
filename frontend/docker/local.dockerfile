FROM node:13.5-buster

ARG APP_DIR=/opt/app
RUN echo "${APP_DIR}"
ENV PATH "$APP_DIR/node_modules/.bin":$PATH

WORKDIR $APP_DIR

COPY ./src/ ./

RUN npm ci

EXPOSE 80

CMD npm start

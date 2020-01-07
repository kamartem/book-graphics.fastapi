FROM nginx:1.17.6-alpine

RUN apk add --no-cache gettext \
    && rm /etc/nginx/conf.d/default.conf

ADD ./docker/nginx.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]

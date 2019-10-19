FROM python:3.7-alpine

COPY ./terra_mars /terra_mars

WORKDIR /terra_mars

RUN apk update

ENV PYTHONUNBUFFERED 1
RUN set -e; \
    apk add --no-cache --virtual .build-deps \
    gcc \
    git \
    libc-dev \
    mariadb-dev \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev \
    ;

RUN pip install -r requirements.txt --src /usr/local/src

# flask Dockerfile
FROM alpine:latest
LABEL maintainer='h-makihara<macky0325@gmail.com>'

# copy source and protocols
WORKDIR /app

# system
RUN apk update \
    && apk upgrade \
    && apk add -U --no-cache perl openssl \
    && apk add --no-cache --virtual .base\
                                    git \
                                    python3 \
                                    py3-pip \
                                    make \
                                    linux-headers \
                                    build-base

RUN apk add --no-cache --virtual .on-build \
                                    curl \
                                    bash

RUN apk add --no-cache --virtual .build-deps \
                                 gcc \
                                 musl-dev \
                                 python3-dev \
                                 openjdk11-jre-headless

# test python client
RUN pip3 install --upgrade pip \
    && pip3 install beautifulsoup4 \
    && pip3 install prettytable \
    && pip3 install pymysql \
    && pip3 install Flask-API \
    && pip3 install tabula-py

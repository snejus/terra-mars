FROM python:3.8-slim

COPY ./terra_mars /terra_mars

WORKDIR /terra_mars

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# TODO: Make multi layered build
RUN pip install -r requirements.txt

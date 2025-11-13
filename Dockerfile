FROM bitnami/python:3.11.3 as base

COPY app /app

USER 11111

WORKDIR /app

ENTRYPOINT [ "python3", "main.py" ]
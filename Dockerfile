FROM bitnami/python:3.11.3 as base

COPY application /application

USER 11111

WORKDIR /application

ENTRYPOINT [ "python3", "main.py" ]
asdasdasd

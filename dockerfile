FROM python:3.12-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.8.3

WORKDIR /src

COPY ./src /src/src
COPY pyproject.toml poetry.lock /src/

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry install --only main

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--forwarded-allow-ips", "*"]
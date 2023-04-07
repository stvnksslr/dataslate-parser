FROM python:3.11 AS build

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.4.2

WORKDIR /src

COPY ./src /src/src/
COPY pyproject.toml poetry.lock /src/

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry install --no-dev


FROM python:3.11-slim-bullseye AS app

COPY --from=build /src/ ./

ENV VIRTUAL_ENV=/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["python", "-m", "src.main"]

FROM python:3.7-alpine as build

WORKDIR /build
COPY Pipfile Pipfile.lock /build/

RUN apk add --update --no-cache g++ gcc libxslt-dev jpeg-dev zlib-dev \
    && pip install pipenv

RUN  PIPENV_VENV_IN_PROJECT=1 pipenv install --dev

FROM python:3.7-alpine as application
WORKDIR /app
COPY --from=build /build /app/
COPY . /app/

RUN apk add --update --no-cache libxslt
RUN .venv/bin/python -mpytest
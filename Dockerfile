FROM python:3.7-slim-stretch as build
ENV PIPENV_VENV_IN_PROJECT=1
ENV PATH=".venv/bin:$PATH"

WORKDIR /build
COPY Pipfile Pipfile.lock /build/

RUN apt-get update -yq
RUN apt-get install --no-install-recommends -yq gcc libxml2-dev libxmlsec1-dev zlib1g-dev
RUN pip install pipenv

RUN pipenv lock -r > requirements.txt  \
    &&  pipenv lock -r --dev > dev-requirements.txt

RUN pip install -r requirements.txt && pip install -r dev-requirements.txt

FROM python:3.7-slim-stretch as ci

WORKDIR /application
COPY --from=build /build/.venv /venv
COPY . /application/

ENV PATH="/venv/bin:$PATH"
RUN python -m pytest
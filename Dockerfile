FROM python:3.8-slim-buster

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /src

COPY ./src /src/src
COPY pyproject.toml poetry.lock /src/

RUN pip install --no-cache-dir poetry
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--forwarded-allow-ips", "*"]
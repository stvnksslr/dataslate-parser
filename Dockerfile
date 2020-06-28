# build stage
FROM python:3.8.3-slim-buster as build

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

COPY ./app /app/app
COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install --user -r requirements.txt

# runner stage
FROM python:3.8.3-slim-buster as run

WORKDIR /app

COPY --from=build /root/.local /root/.local
COPY ./app /app/app

EXPOSE 80

ENV PATH=/root/.local/bin:$PATH

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--forwarded-allow-ips", "*"]
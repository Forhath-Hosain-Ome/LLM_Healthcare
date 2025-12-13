FROM python:3.12-slim

RUN apt-get update && apt-get install -y \ 
    gcc \
    && rm -rf /ver/lib/apt/lists/*

RUN pip install --upgrade pipenv

COPY Pipfile ./

RUN pipenv install --deploy --ignore-Pipfile

COPY . .

EXPOSE 8081
FROM python:3.8.1

ENV PYTHONUNBUFFERED 1

EXPOSE 8080
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.0.* && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./

CMD uvicorn --host=0.0.0.0 --port 8080 app.main:app

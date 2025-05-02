FROM python:3.11.0

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install uv && \
    uv pip install -e .  # Installs dependencies using uv

ARG DEV=false
RUN if [ "$DEV" = "true" ] ; then uv pip install -e .[dev] ; fi

COPY ./app/ ./
COPY ./ml/model/ ./ml/model/

ENV PYTHONPATH "${PYTHONPATH}:/app"

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
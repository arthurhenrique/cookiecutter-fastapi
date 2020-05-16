SHELL := /bin/bash

# Variables definitions
# -----------------------------------------------------------------------------

ifeq ($(TIMEOUT),)
TIMEOUT := 60
endif

# Target section and Global definitions
# -----------------------------------------------------------------------------
LOCAL_PATH_MODEL = /opt/ml/model

.PHONY: all clean test install run deploy down easter

all: clean test install run deploy down easter

test:
	poetry run pytest tests -vv --show-capture=all

install:
	@$(MAKE) generate_dot_env
	pip install --upgrade pip
	pip install poetry
	poetry install

run:
	poetry run uvicorn app.main:app --port 8080 --reload

deploy: generate_dot_env
	docker-compose build
	docker-compose up -d
	@$(MAKE) easter

down:
	docker-compose down

generate_dot_env:
	cp .env.example .env

easter:
	@$(SHELL) egg.sh

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
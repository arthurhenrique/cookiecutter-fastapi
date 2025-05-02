SHELL := /bin/bash

# Variables definitions
# -----------------------------------------------------------------------------

ifeq ($(TIMEOUT),)
TIMEOUT := 60
endif

ifeq ($(MODEL_PATH),)
MODEL_PATH := {{cookiecutter.machine_learn_model_path}}
endif

ifeq ($(MODEL_NAME),)
MODEL_NAME := {{cookiecutter.machine_learn_model_name}}
endif

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install run deploy down

all: clean test install run deploy down

venv:
	uv venv .venv

test: install
	uv run pytest tests -vv --show-capture=all

install: generate_dot_env venv
	pip install uv --break-system-packages
	uv pip install -e ".[dev]"

run: venv
	PYTHONPATH=app/ uv run uvicorn main:app --reload --host 0.0.0.0 --port 8080

deploy: generate_dot_env
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

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

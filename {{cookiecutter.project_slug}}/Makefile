SHELL := /bin/bash
.PHONY: all clean test install run deploy down easter

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

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

deploy:
	@$(MAKE) generate_dot_env
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
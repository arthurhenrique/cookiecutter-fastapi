# cookiecutter-fastapi

In order to create an template to FastAPI projects. :rocket:

## Cookiecutter


```bash
pip install cookiecutter

cookiecutter https://github.com/arthurhenrique/cookiecutter-fastapi.git
```

## Development Requirements

- Python3.8.1
- Pip
- Poetry (Python Package Manager)

## Installation

`make install`

## Runnning Localhost

`make run`

## Deploy app

`make deploy`

## Running Tests

`make test`

## Runnning Easter Egg

`make easter`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

    app
    ├── api              - web related stuff.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── models           - pydantic models for this application.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
    ├──
    tests                - pytest  

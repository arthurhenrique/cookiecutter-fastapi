# fastapi-boilerplate
In order to create an template to FastAPI projects. :rocket:


## Development Requirements
- Python3.8.1
- Pip
- Poetry (Python Package Manager)

## Installation
> `make install`

## Runnning Localhost
> `make run`

## Deploy app
> `make deploy`

## Running Tests
> `make test`

## Access Swagger Documentation
> <http://localhost:8080/docs>


## Or Access Redocs Documentation
> <http://localhost:8080/docs>

Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

    app
    ├── api              - web related stuff.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── models           - pydantic models for this application.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
    ├──
    tests                - pytest  
    
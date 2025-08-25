from fastapi import FastAPI

from core import events
from main import get_application
import services.predict as predict


def test_preload_model(monkeypatch):
    called = {}

    def fake_get_model(cls, loader):
        called["called"] = True

    monkeypatch.setattr(
        predict.MachineLearningModelHandlerScore,
        "get_model",
        classmethod(fake_get_model),
    )
    events.preload_model()
    assert called.get("called") is True


def test_create_start_app_handler(monkeypatch):
    called = {}

    def fake_preload():
        called["called"] = True

    monkeypatch.setattr(events, "preload_model", fake_preload)
    app = FastAPI()
    handler = events.create_start_app_handler(app)
    handler()
    assert called.get("called") is True


def test_get_application():
    app = get_application()
    assert isinstance(app, FastAPI)

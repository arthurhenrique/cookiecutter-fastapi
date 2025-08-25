from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

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

    def fake_create_all(*args, **kwargs):
        raise OperationalError("stmt", {}, Exception("db down"))

    monkeypatch.setattr(events.Base.metadata, "create_all", fake_create_all)

    app = FastAPI()
    handler = events.create_start_app_handler(app)
    handler()
    assert called.get("called") is True


def test_get_application():
    app = get_application()
    assert isinstance(app, FastAPI)

import json
import pytest
from fastapi.testclient import TestClient

from main import get_application
import api.routes.predictor as predictor
from core import config as app_config
import main as app_main


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(app_config, "MEMOIZATION_FLAG", False)
    monkeypatch.setattr(app_main, "MEMOIZATION_FLAG", False)
    app = get_application()
    return TestClient(app)


@pytest.fixture
def anyio_backend():
    return "asyncio"


def sample_payload():
    return {
        "feature1": 1.0,
        "feature2": 2.0,
        "feature3": 3.0,
        "feature4": 4.0,
        "feature5": 5.0,
    }


@pytest.mark.anyio
async def test_predict_endpoint_success(monkeypatch):
    monkeypatch.setattr(predictor, "get_prediction", lambda data: [1])
    data = predictor.MachineLearningDataInput(**sample_payload())
    resp = await predictor.predict(data)
    assert resp.prediction == 1.0
    assert resp.prediction_label == "label ok"


def test_predict_endpoint_exception(client, monkeypatch):
    def raise_error(data):
        raise ValueError("fail")

    monkeypatch.setattr(predictor, "get_prediction", raise_error)
    response = client.post("/api/v1/predict", json=sample_payload())
    assert response.status_code == 500


def test_health_endpoint_success(client, monkeypatch, tmp_path):
    example = tmp_path / "example.json"
    example.write_text(json.dumps(sample_payload()))
    monkeypatch.setattr(predictor, "INPUT_EXAMPLE", str(example))
    monkeypatch.setattr(predictor, "get_prediction", lambda data: [0])
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": True}


def test_health_endpoint_failure(client, monkeypatch):
    monkeypatch.setattr(predictor, "INPUT_EXAMPLE", "missing.json")
    response = client.get("/api/v1/health")
    assert response.status_code == 404

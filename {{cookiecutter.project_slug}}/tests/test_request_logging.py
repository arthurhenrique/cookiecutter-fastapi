import json

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.routes import predictor
from db import Base
from models.log import RequestLog
from models.prediction import MachineLearningDataInput


@pytest.fixture
def anyio_backend():
    return "asyncio"

@pytest.mark.anyio
async def test_predict_logs_request_response(monkeypatch):
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    Base.metadata.create_all(bind=engine)
    monkeypatch.setattr(predictor, "SessionLocal", TestingSessionLocal)
    monkeypatch.setattr(predictor, "get_prediction", lambda data: [1])

    payload = {
        "feature1": 1.0,
        "feature2": 2.0,
        "feature3": 3.0,
        "feature4": 4.0,
        "feature5": 5.0,
    }
    data = MachineLearningDataInput(**payload)

    response = await predictor.predict(data)
    assert response.prediction == 1.0

    db = TestingSessionLocal()
    logs = db.query(RequestLog).all()
    assert len(logs) == 1
    log = logs[0]
    assert json.loads(log.request) == data.model_dump()
    assert json.loads(log.response) == response.model_dump()
    db.close()

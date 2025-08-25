import os

import pytest

import services.predict as predict


class DummyModel:
    def predict(self, data):
        return [42]


class DummyScaler:
    def transform(self, data):
        return data


def test_predict_success(monkeypatch):
    predict.MachineLearningModelHandlerScore.model = DummyModel()
    result = predict.MachineLearningModelHandlerScore.predict([[1]])
    assert result == [42]


def test_predict_missing_method(monkeypatch):
    predict.MachineLearningModelHandlerScore.model = {"model": object(), "scaler": DummyScaler()}
    with pytest.raises(predict.PredictException):
        predict.MachineLearningModelHandlerScore.predict([[1]])


def test_get_model_caches(monkeypatch):
    predict.MachineLearningModelHandlerScore.model = None
    monkeypatch.setattr(
        predict.MachineLearningModelHandlerScore,
        "load",
        staticmethod(lambda loader: {"model": DummyModel(), "scaler": DummyScaler()}),
    )
    model = predict.MachineLearningModelHandlerScore.get_model(lambda path: None)
    assert model["model"].__class__ is DummyModel
    model2 = predict.MachineLearningModelHandlerScore.get_model(None)
    assert model2 is model


def test_load_model_success(tmp_path, monkeypatch):
    dummy = tmp_path / "model.joblib"
    dummy.write_text("data")
    monkeypatch.setattr(predict, "MODEL_PATH", str(tmp_path))
    monkeypatch.setattr(predict, "MODEL_NAME", "model.joblib")

    def fake_loader(path):
        assert os.path.exists(path)
        return {"model": DummyModel(), "scaler": DummyScaler()}

    model = predict.MachineLearningModelHandlerScore.load(fake_loader)
    assert model["model"].__class__ is DummyModel


def test_load_model_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(predict, "MODEL_PATH", str(tmp_path))
    monkeypatch.setattr(predict, "MODEL_NAME", "missing.joblib")
    with pytest.raises(FileNotFoundError):
        predict.MachineLearningModelHandlerScore.load(lambda p: None)


def test_load_model_empty(tmp_path, monkeypatch):
    dummy = tmp_path / "model.joblib"
    dummy.write_text("data")
    monkeypatch.setattr(predict, "MODEL_PATH", str(tmp_path))
    monkeypatch.setattr(predict, "MODEL_NAME", "model.joblib")

    def fake_loader(path):
        return None

    with pytest.raises(predict.ModelLoadException):
        predict.MachineLearningModelHandlerScore.load(fake_loader)

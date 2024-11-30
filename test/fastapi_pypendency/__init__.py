from fastapi import FastAPI
from fastapi_pypendency import Pypendency, get_container


def test_pypendency_initialization_without_app():
    pypendency = Pypendency(app=None, discover_paths=["/path/to/dependencies"])
    assert pypendency.app is None
    assert pypendency.container is None


def test_pypendency_initialization_with_app():
    app = FastAPI()
    pypendency = Pypendency(app=app, discover_paths=["/path/to/dependencies"])
    assert pypendency.app == app
    assert hasattr(app, "pypendency")
    assert app.pypendency == pypendency
    assert app.pypendency.container is not None

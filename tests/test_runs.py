from fastapi.testclient import TestClient
from main import app


def test_get_all_runs():
    with TestClient(app) as client:
        resp = client.get("/all_runs")
        assert resp.status_code == 200
        assert isinstance(resp.json(), list)


def test_get_stats():
    with TestClient(app) as client:
        resp = client.get("/stats")
        assert resp.status_code == 200
        assert isinstance(resp.json(), dict)

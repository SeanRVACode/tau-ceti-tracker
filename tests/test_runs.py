from fastapi.testclient import TestClient
from fastapi import Request
from main import app
from auth import require_auth


# Fake data for testing purposes.
DATA = {
    "shell": "destroyer",
    "map_name": "outpost",
    "exfiled": False,
    "exfil_amount": 0,
    "rook_friends": False,
    "team_mates_rezzed": 0,
    "runner_downs": 2,
    "uesc_elims": 12,
}


async def override_dependency(req: Request):
    req.session["user"] = "test@email.com"


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


def test_post_with_auth():
    app.dependency_overrides[require_auth] = override_dependency
    with TestClient(app) as client:
        resp = client.post("/run", json=DATA)
        assert resp.status_code == 200


def test_post_without_auth():
    # Clear the overrides
    app.dependency_overrides = {}
    # Run the test with now that there is no override.
    with TestClient(app) as client:
        resp = client.post("/run", json=DATA)
        assert resp.status_code == 401

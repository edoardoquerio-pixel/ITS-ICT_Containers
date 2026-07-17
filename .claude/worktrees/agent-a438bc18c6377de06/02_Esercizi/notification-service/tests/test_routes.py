"""Test degli endpoint REST per Notification Service."""


def test_health_check(client):
    """GET /health restituisce 200 OK."""
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_readiness_check(client):
    """GET /ready restituisce 200 con database connesso."""
    resp = client.get("/ready")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["database"] == "connected"


class TestSendNotification:
    def test_sent(self, client):
        resp = client.post("/notifications", json={"user_id": 1, "channel": "email", "message": "Ciao!"})
        assert resp.status_code == 201
        data = resp.json()
        assert data["user_id"] == 1
        assert data["channel"] == "email"
        assert data["message"] == "Ciao!"
        assert data["status"] == "sent"
        assert "id" in data

    def test_default_channel(self, client):
        resp = client.post("/notifications", json={"user_id": 1, "message": "Test"})
        assert resp.status_code == 201
        assert resp.json()["channel"] == "email"


class TestListNotifications:
    def test_empty(self, client):
        resp = client.get("/notifications")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_multiple(self, client):
        client.post("/notifications", json={"user_id": 1, "message": "A"})
        client.post("/notifications", json={"user_id": 2, "message": "B"})
        resp = client.get("/notifications")
        assert len(resp.json()) == 2

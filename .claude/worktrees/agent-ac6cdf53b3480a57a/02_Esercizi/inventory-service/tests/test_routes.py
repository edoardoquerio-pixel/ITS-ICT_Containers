"""Test degli endpoint REST per Inventory Service."""


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


class TestSetStock:
    def test_created(self, client):
        resp = client.post("/inventory", json={"book_id": 1, "quantity": 10})
        assert resp.status_code == 201
        data = resp.json()
        assert data["book_id"] == 1
        assert data["quantity"] == 10
        assert "id" in data

    def test_update(self, client):
        client.post("/inventory", json={"book_id": 1, "quantity": 10})
        resp = client.post("/inventory", json={"book_id": 1, "quantity": 5})
        assert resp.status_code == 201
        assert resp.json()["quantity"] == 5


class TestGetStock:
    def test_found(self, client):
        client.post("/inventory", json={"book_id": 1, "quantity": 10})
        resp = client.get("/inventory/1")
        assert resp.status_code == 200
        assert resp.json()["quantity"] == 10

    def test_not_found(self, client):
        resp = client.get("/inventory/99999")
        assert resp.status_code == 404


class TestListInventory:
    def test_empty(self, client):
        resp = client.get("/inventory")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_multiple(self, client):
        client.post("/inventory", json={"book_id": 1, "quantity": 10})
        client.post("/inventory", json={"book_id": 2, "quantity": 5})
        resp = client.get("/inventory")
        assert len(resp.json()) == 2

"""Test degli endpoint REST per Loan Service."""


def test_health_check(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_readiness_check(client):
    resp = client.get("/ready")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["database"] == "connected"


class TestCreateLoan:
    def test_created(self, client):
        resp = client.post("/loans", json={"user_id": 1, "book_id": 1})
        assert resp.status_code == 201
        data = resp.json()
        assert data["user_id"] == 1
        assert data["book_id"] == 1
        assert data["active"] is True

    def test_missing_fields(self, client):
        resp = client.post("/loans", json={})
        assert resp.status_code == 422

    def test_invalid_user_id(self, client):
        resp = client.post("/loans", json={"user_id": 0, "book_id": 1})
        assert resp.status_code == 422


class TestListLoans:
    def test_empty(self, client):
        resp = client.get("/loans")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_multiple(self, client):
        client.post("/loans", json={"user_id": 1, "book_id": 1})
        client.post("/loans", json={"user_id": 2, "book_id": 2})
        resp = client.get("/loans")
        assert len(resp.json()) == 2


class TestGetLoan:
    def test_found(self, client):
        created = client.post("/loans", json={"user_id": 1, "book_id": 1}).json()
        resp = client.get(f"/loans/{created['id']}")
        assert resp.status_code == 200

    def test_not_found(self, client):
        resp = client.get("/loans/99999")
        assert resp.status_code == 404


class TestReturnLoan:
    def test_returned(self, client):
        created = client.post("/loans", json={"user_id": 1, "book_id": 1}).json()
        resp = client.put(f"/loans/{created['id']}/return")
        assert resp.status_code == 200
        assert resp.json()["active"] is False

    def test_return_not_found(self, client):
        resp = client.put("/loans/99999/return")
        assert resp.status_code == 404

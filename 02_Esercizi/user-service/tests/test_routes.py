"""Test degli endpoint REST per User Service."""


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


class TestCreateUser:
    def test_created(self, client):
        resp = client.post("/users", json={"name": "Mario", "email": "mario@test.it"})
        assert resp.status_code == 201
        data = resp.json()
        assert data["name"] == "Mario"
        assert data["email"] == "mario@test.it"
        assert "id" in data

    def test_duplicate_email(self, client):
        client.post("/users", json={"name": "Mario", "email": "mario@test.it"})
        resp = client.post("/users", json={"name": "Luigi", "email": "mario@test.it"})
        assert resp.status_code == 409

    def test_missing_name(self, client):
        resp = client.post("/users", json={"email": "x@y.it"})
        assert resp.status_code == 422


class TestListUsers:
    def test_empty(self, client):
        resp = client.get("/users")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_multiple(self, client):
        client.post("/users", json={"name": "A", "email": "a@a.it"})
        client.post("/users", json={"name": "B", "email": "b@b.it"})
        resp = client.get("/users")
        assert len(resp.json()) == 2


class TestGetUser:
    def test_found(self, client):
        created = client.post("/users", json={"name": "C", "email": "c@c.it"}).json()
        resp = client.get(f"/users/{created['id']}")
        assert resp.status_code == 200
        assert resp.json()["name"] == "C"

    def test_not_found(self, client):
        resp = client.get("/users/99999")
        assert resp.status_code == 404


class TestDeleteUser:
    def test_deleted(self, client):
        created = client.post("/users", json={"name": "D", "email": "d@d.it"}).json()
        resp = client.delete(f"/users/{created['id']}")
        assert resp.status_code == 204

    def test_not_found(self, client):
        resp = client.delete("/users/99999")
        assert resp.status_code == 404

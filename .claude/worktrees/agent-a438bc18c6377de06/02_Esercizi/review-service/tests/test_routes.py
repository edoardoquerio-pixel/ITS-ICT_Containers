"""Test degli endpoint REST per Review Service."""


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


class TestCreateReview:
    def test_created(self, client):
        resp = client.post("/reviews", json={"book_id": 1, "user_id": 1, "rating": 5, "comment": "Ottimo!"})
        assert resp.status_code == 201
        data = resp.json()
        assert data["rating"] == 5
        assert data["comment"] == "Ottimo!"

    def test_invalid_rating(self, client):
        resp = client.post("/reviews", json={"book_id": 1, "user_id": 1, "rating": 6})
        assert resp.status_code == 422

    def test_missing_fields(self, client):
        resp = client.post("/reviews", json={})
        assert resp.status_code == 422


class TestListReviews:
    def test_empty(self, client):
        resp = client.get("/reviews")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_multiple(self, client):
        client.post("/reviews", json={"book_id": 1, "user_id": 1, "rating": 4})
        client.post("/reviews", json={"book_id": 1, "user_id": 2, "rating": 3})
        resp = client.get("/reviews")
        assert len(resp.json()) == 2


class TestGetReview:
    def test_found(self, client):
        created = client.post("/reviews", json={"book_id": 1, "user_id": 1, "rating": 5}).json()
        resp = client.get(f"/reviews/{created['id']}")
        assert resp.status_code == 200

    def test_not_found(self, client):
        resp = client.get("/reviews/99999")
        assert resp.status_code == 404


class TestGetReviewsByBook:
    def test_by_book(self, client):
        client.post("/reviews", json={"book_id": 10, "user_id": 1, "rating": 4})
        client.post("/reviews", json={"book_id": 10, "user_id": 2, "rating": 5})
        resp = client.get("/reviews/by-book/10")
        assert resp.status_code == 200
        assert len(resp.json()) == 2

    def test_by_book_empty(self, client):
        resp = client.get("/reviews/by-book/999")
        assert resp.status_code == 200
        assert resp.json() == []

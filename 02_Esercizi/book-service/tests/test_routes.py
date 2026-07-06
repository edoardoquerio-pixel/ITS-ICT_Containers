"""Test degli endpoint REST — test di integrazione via TestClient."""


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


class TestCreateBook:
    def test_created(self, client):
        """POST /books/ con dati validi → 201."""
        payload = {
            "titolo": "Il nome della rosa",
            "autore": "Umberto Eco",
            "isbn": "9788845293689",
            "anno_pubblicazione": 1980,
            "genere": "Giallo storico",
            "disponibile": True,
        }
        resp = client.post("/books/", json=payload)
        assert resp.status_code == 201
        data = resp.json()
        assert data["titolo"] == "Il nome della rosa"
        assert data["autore"] == "Umberto Eco"
        assert data["isbn"] == "9788845293689"
        assert data["disponibile"] is True
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data

    def test_duplicate_isbn(self, client):
        """POST /books/ con ISBN duplicato → 409."""
        payload = {
            "titolo": "Il nome della rosa",
            "autore": "Umberto Eco",
            "isbn": "9788845293689",
        }
        client.post("/books/", json=payload)
        resp = client.post("/books/", json=payload)
        assert resp.status_code == 409
        assert "ISBN" in resp.json()["detail"]

    def test_missing_fields(self, client):
        """POST /books/ senza campi obbligatori → 422."""
        resp = client.post("/books/", json={"titolo": "Incompleto"})
        assert resp.status_code == 422


class TestListBooks:
    def test_empty(self, client):
        """GET /books/ senza libri → lista vuota."""
        resp = client.get("/books/")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_multiple(self, client):
        """GET /books/ con più libri."""
        client.post("/books/", json={"titolo": "Libro A", "autore": "A", "isbn": "1111111111"})
        client.post("/books/", json={"titolo": "Libro B", "autore": "B", "isbn": "2222222222"})
        resp = client.get("/books/")
        assert len(resp.json()) == 2

    def test_filter_by_genre(self, client):
        """GET /books/?genere=... filtra correttamente."""
        client.post("/books/", json={"titolo": "Giallo", "autore": "A", "isbn": "1111111111", "genere": "Giallo"})
        client.post("/books/", json={"titolo": "Fantasy", "autore": "B", "isbn": "2222222222", "genere": "Fantasy"})
        resp = client.get("/books/?genere=Giallo")
        data = resp.json()
        assert len(data) == 1
        assert data[0]["titolo"] == "Giallo"

    def test_filter_by_availability(self, client):
        """GET /books/?disponibile=... filtra correttamente."""
        client.post("/books/", json={"titolo": "A", "autore": "A", "isbn": "1111111111", "disponibile": True})
        client.post("/books/", json={"titolo": "B", "autore": "B", "isbn": "2222222222", "disponibile": False})
        resp = client.get("/books/?disponibile=true")
        assert len(resp.json()) == 1

    def test_pagination(self, client):
        """GET /books/?skip=...&limit=... funziona."""
        for i in range(5):
            client.post("/books/", json={"titolo": f"Libro {i}", "autore": "A", "isbn": f"000000{i:04d}0"})
        resp = client.get("/books/?skip=1&limit=2")
        data = resp.json()
        assert len(data) == 2

    def test_pagination_defaults(self, client):
        """GET /books/ senza skip/limit restituisce tutti i libri."""
        for i in range(5):
            client.post("/books/", json={"titolo": f"Libro {i}", "autore": "A", "isbn": f"000000{i:04d}0"})
        resp = client.get("/books/")
        assert len(resp.json()) == 5

    def test_pagination_invalid_limit(self, client):
        """GET /books/?limit=9999 → 422 (max 500)."""
        resp = client.get("/books/?limit=9999")
        assert resp.status_code == 422


class TestGetBook:
    def test_found(self, client):
        """GET /books/{id} → 200 con il libro."""
        create_resp = client.post("/books/", json={"titolo": "Test", "autore": "T", "isbn": "1111111111"})
        book_id = create_resp.json()["id"]
        resp = client.get(f"/books/{book_id}")
        assert resp.status_code == 200
        assert resp.json()["id"] == book_id

    def test_not_found(self, client):
        """GET /books/{id} inesistente → 404."""
        resp = client.get("/books/9999")
        assert resp.status_code == 404


class TestUpdateBook:
    def test_update(self, client):
        """PUT /books/{id} aggiorna il libro."""
        create_resp = client.post("/books/", json={"titolo": "Vecchio", "autore": "A", "isbn": "1111111111"})
        book_id = create_resp.json()["id"]
        resp = client.put(
            f"/books/{book_id}",
            json={"titolo": "Nuovo", "disponibile": False},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["titolo"] == "Nuovo"
        assert data["disponibile"] is False

    def test_not_found(self, client):
        """PUT /books/{id} inesistente → 404."""
        resp = client.put("/books/9999", json={"titolo": "Nuovo"})
        assert resp.status_code == 404

    def test_duplicate_isbn(self, client):
        """PUT /books/{id} con ISBN già usato → 409."""
        client.post("/books/", json={"titolo": "A", "autore": "A", "isbn": "1111111111"})
        resp2 = client.post("/books/", json={"titolo": "B", "autore": "B", "isbn": "2222222222"})
        book2_id = resp2.json()["id"]
        resp = client.put(f"/books/{book2_id}", json={"isbn": "1111111111"})
        assert resp.status_code == 409


class TestDeleteBook:
    def test_deleted(self, client):
        """DELETE /books/{id} → 204."""
        create_resp = client.post("/books/", json={"titolo": "Test", "autore": "T", "isbn": "1111111111"})
        book_id = create_resp.json()["id"]
        resp = client.delete(f"/books/{book_id}")
        assert resp.status_code == 204

    def test_not_found(self, client):
        """DELETE /books/{id} inesistente → 404."""
        resp = client.delete("/books/9999")
        assert resp.status_code == 404

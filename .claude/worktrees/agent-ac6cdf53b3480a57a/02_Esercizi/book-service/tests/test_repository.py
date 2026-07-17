"""Test del repository layer — CRUD con SQLAlchemy."""
from app.repositories import repository
from app.schemas.schemas import BookCreate, BookUpdate

SAMPLE_BOOK = BookCreate(
    titolo="Il nome della rosa",
    autore="Umberto Eco",
    isbn="9788845293689",
    anno_pubblicazione=1980,
    genere="Giallo storico",
    disponibile=True,
)


def test_create_and_get_by_id(test_db):
    """Crea un libro e lo recupera per ID."""
    book = repository.create(test_db, SAMPLE_BOOK)

    assert book.id > 0
    assert book.titolo == "Il nome della rosa"
    assert book.autore == "Umberto Eco"
    assert book.disponibile is True
    assert book.created_at is not None
    assert book.updated_at is not None

    found = repository.get_by_id(test_db, book.id)
    assert found is not None
    assert found.titolo == book.titolo


def test_get_by_id_not_found(test_db):
    """get_by_id restituisce None per ID inesistente."""
    result = repository.get_by_id(test_db, 9999)
    assert result is None


def test_get_all(test_db):
    """get_all restituisce tutti i libri."""
    repository.create(test_db, SAMPLE_BOOK)
    repository.create(
        test_db,
        BookCreate(
            titolo="1984",
            autore="George Orwell",
            isbn="9788807903344",
            anno_pubblicazione=1949,
            genere="Distopia",
            disponibile=True,
        ),
    )

    books = repository.get_all(test_db)
    assert len(books) == 2


def test_get_all_filtered_by_genre(test_db):
    """get_all filtra correttamente per genere."""
    repository.create(test_db, SAMPLE_BOOK)
    repository.create(
        test_db,
        BookCreate(
            titolo="1984",
            autore="George Orwell",
            isbn="9788807903344",
            genere="Distopia",
        ),
    )

    gialli = repository.get_all(test_db, genere="Giallo storico")
    distopie = repository.get_all(test_db, genere="Distopia")
    inesistente = repository.get_all(test_db, genere="Fantasy")

    assert len(gialli) == 1
    assert len(distopie) == 1
    assert len(inesistente) == 0


def test_get_all_filtered_by_availability(test_db):
    """get_all filtra per disponibilità."""
    repository.create(test_db, SAMPLE_BOOK)
    repository.create(
        test_db,
        BookCreate(
            titolo="1984",
            autore="George Orwell",
            isbn="9788807903344",
            disponibile=False,
        ),
    )

    disponibili = repository.get_all(test_db, disponibile=True)
    non_disponibili = repository.get_all(test_db, disponibile=False)

    assert len(disponibili) == 1
    assert len(non_disponibili) == 1


def test_get_all_pagination(test_db):
    """get_all con skip/limit funziona correttamente."""
    for i in range(5):
        isbn = f"000000{i:04d}0"
        repository.create(
            test_db,
            BookCreate(
                titolo=f"Libro {i}",
                autore="Autore",
                isbn=isbn,
            ),
        )

    # Primi 2
    page1 = repository.get_all(test_db, skip=0, limit=2)
    assert len(page1) == 2

    # Skip 2, prendi 2
    page2 = repository.get_all(test_db, skip=2, limit=2)
    assert len(page2) == 2
    assert page2[0].titolo != page1[0].titolo

    # Oltre il totale
    empty = repository.get_all(test_db, skip=10, limit=10)
    assert empty == []


def test_update(test_db):
    """Aggiorna i campi di un libro."""
    book = repository.create(test_db, SAMPLE_BOOK)

    update = BookUpdate(titolo="Il nome della rosa (Edizione speciale)", disponibile=False)
    updated = repository.update(test_db, book.id, update)

    assert updated is not None
    assert updated.titolo == "Il nome della rosa (Edizione speciale)"
    assert updated.disponibile is False
    assert updated.autore == "Umberto Eco"
    assert updated.isbn == "9788845293689"


def test_update_not_found(test_db):
    """update restituisce None per ID inesistente."""
    update = BookUpdate(titolo="Nuovo titolo")
    result = repository.update(test_db, 9999, update)
    assert result is None


def test_update_no_changes(test_db):
    """update senza modifiche restituisce il record originale."""
    book = repository.create(test_db, SAMPLE_BOOK)

    update = BookUpdate()
    result = repository.update(test_db, book.id, update)

    assert result is not None
    assert result.titolo == book.titolo
    assert result.disponibile == book.disponibile


def test_delete(test_db):
    """Elimina un libro e verifica che non sia più presente."""
    book = repository.create(test_db, SAMPLE_BOOK)

    deleted = repository.delete(test_db, book.id)
    assert deleted is True

    found = repository.get_by_id(test_db, book.id)
    assert found is None


def test_delete_not_found(test_db):
    """delete restituisce False per ID inesistente."""
    result = repository.delete(test_db, 9999)
    assert result is False


def test_get_by_isbn(test_db):
    """get_by_isbn restituisce un libro per ISBN."""
    repository.create(test_db, SAMPLE_BOOK)
    found = repository.get_by_isbn(test_db, "9788845293689")
    assert found is not None
    assert found.titolo == "Il nome della rosa"

    missing = repository.get_by_isbn(test_db, "0000000000000")
    assert missing is None

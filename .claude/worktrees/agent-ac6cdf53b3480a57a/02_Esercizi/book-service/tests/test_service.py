"""Test del service layer — logica di business e HTTPException."""
import pytest
from fastapi import HTTPException

from app.schemas.schemas import BookCreate, BookUpdate
from app.services import service as book_service

SAMPLE_BOOK = BookCreate(
    titolo="Il nome della rosa",
    autore="Umberto Eco",
    isbn="9788845293689",
    anno_pubblicazione=1980,
    genere="Giallo storico",
)


def test_create_book(test_db):
    """Crea un libro con successo."""
    book = book_service.create_book(test_db, SAMPLE_BOOK)
    assert book.id > 0
    assert book.titolo == "Il nome della rosa"
    assert book.isbn == "9788845293689"


def test_create_duplicate_isbn(test_db):
    """ISBN duplicato solleva HTTPException 409."""
    book_service.create_book(test_db, SAMPLE_BOOK)
    with pytest.raises(HTTPException) as exc:
        book_service.create_book(test_db, SAMPLE_BOOK)
    assert exc.value.status_code == 409
    assert "ISBN" in exc.value.detail


def test_get_book(test_db):
    """Recupera un libro esistente."""
    book = book_service.create_book(test_db, SAMPLE_BOOK)
    found = book_service.get_book(test_db, book.id)
    assert found.id == book.id
    assert found.titolo == book.titolo


def test_get_book_not_found(test_db):
    """Libro inesistente solleva HTTPException 404."""
    with pytest.raises(HTTPException) as exc:
        book_service.get_book(test_db, 9999)
    assert exc.value.status_code == 404


def test_get_books(test_db):
    """Lista libri senza filtri."""
    book_service.create_book(test_db, SAMPLE_BOOK)
    book_service.create_book(
        test_db,
        BookCreate(titolo="1984", autore="George Orwell", isbn="9788807903344"),
    )
    books = book_service.get_books(test_db)
    assert len(books) == 2


def test_get_books_filtered(test_db):
    """Lista libri con filtro genere."""
    book_service.create_book(test_db, SAMPLE_BOOK)
    book_service.create_book(
        test_db,
        BookCreate(titolo="1984", autore="George Orwell", isbn="9788807903344", genere="Distopia"),
    )
    gialli = book_service.get_books(test_db, genere="Giallo storico")
    assert len(gialli) == 1
    assert gialli[0].isbn == "9788845293689"


def test_get_books_pagination(test_db):
    """Lista libri con paginazione."""
    for i in range(5):
        book_service.create_book(
            test_db,
            BookCreate(
                titolo=f"Libro {i}",
                autore="Autore",
                isbn=f"000000{i:04d}0",
            ),
        )

    page = book_service.get_books(test_db, skip=1, limit=2)
    assert len(page) == 2


def test_update_book(test_db):
    """Aggiorna un libro con successo."""
    book = book_service.create_book(test_db, SAMPLE_BOOK)
    updated = book_service.update_book(test_db, book.id, BookUpdate(titolo="Nuovo titolo", disponibile=False))
    assert updated.titolo == "Nuovo titolo"
    assert updated.disponibile is False
    assert updated.autore == "Umberto Eco"


def test_update_book_not_found(test_db):
    """Aggiornamento libro inesistente solleva 404."""
    with pytest.raises(HTTPException) as exc:
        book_service.update_book(test_db, 9999, BookUpdate(titolo="Nuovo"))
    assert exc.value.status_code == 404


def test_update_duplicate_isbn(test_db):
    """Aggiornamento con ISBN già usato solleva 409."""
    book_service.create_book(test_db, SAMPLE_BOOK)
    book2 = book_service.create_book(
        test_db,
        BookCreate(titolo="1984", autore="Orwell", isbn="9788807903344"),
    )
    with pytest.raises(HTTPException) as exc:
        book_service.update_book(test_db, book2.id, BookUpdate(isbn="9788845293689"))
    assert exc.value.status_code == 409


def test_delete_book(test_db):
    """Elimina un libro con successo."""
    book = book_service.create_book(test_db, SAMPLE_BOOK)
    book_service.delete_book(test_db, book.id)
    with pytest.raises(HTTPException) as exc:
        book_service.get_book(test_db, book.id)
    assert exc.value.status_code == 404


def test_delete_book_not_found(test_db):
    """Eliminazione libro inesistente solleva 404."""
    with pytest.raises(HTTPException) as exc:
        book_service.delete_book(test_db, 9999)
    assert exc.value.status_code == 404

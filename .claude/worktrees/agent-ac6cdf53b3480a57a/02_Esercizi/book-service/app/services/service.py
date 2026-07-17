"""Service layer per il Book.

Contiene la logica di business e coordina le operazioni
tra api e repository. Usa SQLAlchemy session.
"""
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import repository
from app.schemas.schemas import Book, BookCreate, BookUpdate


def create_book(db: Session, book_in: BookCreate) -> Book:
    """Crea un nuovo libro.

    Solleva HTTPException 409 se l'ISBN esiste già.
    """
    existing = repository.get_by_isbn(db, book_in.isbn)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"ISBN '{book_in.isbn}' già presente nel sistema",
        )
    return repository.create(db, book_in)


def get_book(db: Session, book_id: int) -> Book:
    """Restituisce un libro per ID.

    Solleva HTTPException 404 se non trovato.
    """
    book = repository.get_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con id {book_id} non trovato",
        )
    return book


def get_books(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    genere: Optional[str] = None,
    disponibile: Optional[bool] = None,
) -> list[Book]:
    """Restituisce la lista dei libri, con paginazione e filtri opzionali."""
    return repository.get_all(db, skip=skip, limit=limit, genere=genere, disponibile=disponibile)


def update_book(db: Session, book_id: int, book_in: BookUpdate) -> Book:
    """Aggiorna un libro (solo i campi forniti).

    Solleva HTTPException 404 se non trovato,
    409 se il nuovo ISBN è già usato da un altro libro.
    """
    if book_in.isbn:
        existing = repository.get_by_isbn(db, book_in.isbn)
        if existing and existing.id != book_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"ISBN '{book_in.isbn}' già assegnato a un altro libro",
            )

    book = repository.update(db, book_id, book_in)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con id {book_id} non trovato",
        )
    return book


def delete_book(db: Session, book_id: int) -> None:
    """Elimina un libro per ID.

    Solleva HTTPException 404 se non trovato.
    """
    deleted = repository.delete(db, book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con id {book_id} non trovato",
        )

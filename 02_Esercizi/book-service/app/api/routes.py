"""Route REST per il Book Service.

Definisce gli endpoint CRUD per la risorsa Book.
Usa Dependency Injection per la sessione SQLAlchemy.
"""
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import Book, BookCreate, BookUpdate
from app.services import service as book_service

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[Book])
def list_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    genere: Optional[str] = Query(None),
    disponibile: Optional[bool] = Query(None),
    db: Session = Depends(get_db),
):
    """Restituisce l'elenco dei libri. Paginazione e filtri opzionali."""
    return book_service.get_books(db, skip=skip, limit=limit, genere=genere, disponibile=disponibile)


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Restituisce un libro specifico per ID."""
    return book_service.get_book(db, book_id)


@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookCreate, db: Session = Depends(get_db)):
    """Crea un nuovo libro. 409 se ISBN duplicato."""
    return book_service.create_book(db, book_in)


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book_in: BookUpdate, db: Session = Depends(get_db)):
    """Aggiorna un libro. 404 se non trovato, 409 se ISBN duplicato."""
    return book_service.update_book(db, book_id, book_in)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Elimina un libro. 404 se non trovato."""
    book_service.delete_book(db, book_id)

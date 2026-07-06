"""Service layer per l'Inventory.

Contiene la logica di business e coordina le operazioni
tra api e repository. Usa SQLAlchemy session.
"""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import repository
from app.schemas.schemas import StockCreate, StockEntry


def set_stock(db: Session, stock_in: StockCreate) -> StockEntry:
    """Imposta (crea o aggiorna) le scorte per un libro."""
    return repository.upsert(db, stock_in)


def get_stock(db: Session, book_id: int) -> StockEntry:
    """Restituisce le scorte per un libro.

    Solleva HTTPException 404 se non trovato.
    """
    entry = repository.get_by_book_id(db, book_id)
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con id {book_id} non trovato nell'inventario",
        )
    return entry


def get_all_stock(db: Session) -> list[StockEntry]:
    """Restituisce tutte le scorte."""
    return repository.get_all(db)

"""Repository per l'entità Inventory.

Fornisce metodi CRUD usando SQLAlchemy ORM.
"""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import InventoryORM
from app.schemas.schemas import StockCreate, StockEntry


def _orm_to_schema(orm: InventoryORM) -> StockEntry:
    """Converte un modello ORM in schema Pydantic."""
    return StockEntry(
        id=orm.id,
        book_id=orm.book_id,
        quantity=orm.quantity,
        created_at=orm.created_at,
        updated_at=orm.updated_at,
    )


def upsert(db: Session, stock_in: StockCreate) -> StockEntry:
    """Inserisce o aggiorna le scorte per un libro."""
    orm = db.execute(
        select(InventoryORM).where(InventoryORM.book_id == stock_in.book_id)
    ).scalar_one_or_none()

    if orm:
        orm.quantity = stock_in.quantity
    else:
        orm = InventoryORM(
            book_id=stock_in.book_id,
            quantity=stock_in.quantity,
        )
        db.add(orm)

    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)


def get_by_book_id(db: Session, book_id: int) -> Optional[StockEntry]:
    """Restituisce le scorte per book_id, o None se non trovato."""
    orm = db.execute(
        select(InventoryORM).where(InventoryORM.book_id == book_id)
    ).scalar_one_or_none()
    return _orm_to_schema(orm) if orm else None


def get_all(db: Session) -> list[StockEntry]:
    """Restituisce tutte le scorte."""
    stmt = select(InventoryORM).order_by(InventoryORM.book_id.asc())
    orms = db.execute(stmt).scalars().all()
    return [_orm_to_schema(o) for o in orms]

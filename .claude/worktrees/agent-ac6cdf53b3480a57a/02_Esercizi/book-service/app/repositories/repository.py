"""Repository per l'entità Book.

Fornisce metodi CRUD usando SQLAlchemy ORM.
Ogni metodo riceve una sessione SQLAlchemy (dependency injection).
"""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import BookORM
from app.schemas.schemas import Book, BookCreate, BookUpdate


def _orm_to_schema(orm: BookORM) -> Book:
    """Converte un modello ORM in schema Pydantic."""
    return Book(
        id=orm.id,
        titolo=orm.titolo,
        autore=orm.autore,
        isbn=orm.isbn,
        anno_pubblicazione=orm.anno_pubblicazione,
        genere=orm.genere,
        disponibile=orm.disponibile,
        created_at=orm.created_at,
        updated_at=orm.updated_at,
    )


def create(db: Session, book_in: BookCreate) -> Book:
    """Inserisce un nuovo libro e restituisce il record completo."""
    orm = BookORM(
        titolo=book_in.titolo,
        autore=book_in.autore,
        isbn=book_in.isbn,
        anno_pubblicazione=book_in.anno_pubblicazione,
        genere=book_in.genere,
        disponibile=book_in.disponibile,
    )
    db.add(orm)
    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)


def get_by_id(db: Session, book_id: int) -> Optional[Book]:
    """Restituisce un libro per ID, o None se non trovato."""
    orm = db.get(BookORM, book_id)
    return _orm_to_schema(orm) if orm else None


def get_all(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    genere: Optional[str] = None,
    disponibile: Optional[bool] = None,
) -> list[Book]:
    """Restituisce tutti i libri, con paginazione e filtri opzionali."""
    stmt = select(BookORM)

    if genere:
        stmt = stmt.where(BookORM.genere == genere)
    if disponibile is not None:
        stmt = stmt.where(BookORM.disponibile == disponibile)

    stmt = stmt.order_by(BookORM.titolo.asc()).offset(skip).limit(limit)
    orms = db.execute(stmt).scalars().all()
    return [_orm_to_schema(o) for o in orms]


def update(db: Session, book_id: int, book_in: BookUpdate) -> Optional[Book]:
    """Aggiorna un libro (solo i campi non-None) e restituisce il record."""
    orm = db.get(BookORM, book_id)
    if not orm:
        return None

    update_data = book_in.model_dump(exclude_unset=True)
    if not update_data:
        return _orm_to_schema(orm)

    for field, value in update_data.items():
        setattr(orm, field, value)

    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)


def delete(db: Session, book_id: int) -> bool:
    """Elimina un libro per ID. Restituisce True se cancellato."""
    orm = db.get(BookORM, book_id)
    if not orm:
        return False
    db.delete(orm)
    db.commit()
    return True


def get_by_isbn(db: Session, isbn: str) -> Optional[Book]:
    """Cerca un libro per ISBN. Usato per validazione unicità."""
    stmt = select(BookORM).where(BookORM.isbn == isbn)
    orm = db.execute(stmt).scalar_one_or_none()
    return _orm_to_schema(orm) if orm else None

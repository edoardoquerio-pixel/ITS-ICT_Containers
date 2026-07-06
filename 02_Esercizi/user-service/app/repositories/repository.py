"""Repository per l'entità User.

Fornisce metodi CRUD usando SQLAlchemy ORM.
"""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import UserORM
from app.schemas.schemas import User, UserCreate, UserUpdate


def _orm_to_schema(orm: UserORM) -> User:
    """Converte un modello ORM in schema Pydantic."""
    return User(
        id=orm.id,
        name=orm.name,
        email=orm.email,
        created_at=orm.created_at,
        updated_at=orm.updated_at,
    )


def create(db: Session, user_in: UserCreate) -> User:
    """Inserisce un nuovo utente e restituisce il record completo."""
    orm = UserORM(
        name=user_in.name,
        email=user_in.email,
    )
    db.add(orm)
    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)


def get_by_id(db: Session, user_id: int) -> Optional[User]:
    """Restituisce un utente per ID, o None se non trovato."""
    orm = db.get(UserORM, user_id)
    return _orm_to_schema(orm) if orm else None


def get_all(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[User]:
    """Restituisce tutti gli utenti, con paginazione."""
    stmt = select(UserORM).order_by(UserORM.name.asc()).offset(skip).limit(limit)
    orms = db.execute(stmt).scalars().all()
    return [_orm_to_schema(o) for o in orms]


def get_by_email(db: Session, email: str) -> Optional[User]:
    """Cerca un utente per email. Usato per validazione unicità."""
    stmt = select(UserORM).where(UserORM.email == email)
    orm = db.execute(stmt).scalar_one_or_none()
    return _orm_to_schema(orm) if orm else None


def update(db: Session, user_id: int, user_in: UserUpdate) -> Optional[User]:
    """Aggiorna un utente (solo i campi non-None) e restituisce il record."""
    orm = db.get(UserORM, user_id)
    if not orm:
        return None

    update_data = user_in.model_dump(exclude_unset=True)
    if not update_data:
        return _orm_to_schema(orm)

    for field, value in update_data.items():
        setattr(orm, field, value)

    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)


def delete(db: Session, user_id: int) -> bool:
    """Elimina un utente per ID. Restituisce True se cancellato."""
    orm = db.get(UserORM, user_id)
    if not orm:
        return False
    db.delete(orm)
    db.commit()
    return True

"""Service layer per lo User.

Contiene la logica di business e coordina le operazioni
tra api e repository. Usa SQLAlchemy session.
"""
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import repository
from app.schemas.schemas import User, UserCreate, UserUpdate


def create_user(db: Session, user_in: UserCreate) -> User:
    """Crea un nuovo utente.

    Solleva HTTPException 409 se l'email esiste già.
    """
    existing = repository.get_by_email(db, user_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Email '{user_in.email}' già presente nel sistema",
        )
    return repository.create(db, user_in)


def get_user(db: Session, user_id: int) -> User:
    """Restituisce un utente per ID.

    Solleva HTTPException 404 se non trovato.
    """
    user = repository.get_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Utente con id {user_id} non trovato",
        )
    return user


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[User]:
    """Restituisce la lista degli utenti, con paginazione."""
    return repository.get_all(db, skip=skip, limit=limit)


def update_user(db: Session, user_id: int, user_in: UserUpdate) -> User:
    """Aggiorna un utente (solo i campi forniti).

    Solleva HTTPException 404 se non trovato,
    409 se la nuova email è già usata da un altro utente.
    """
    if user_in.email:
        existing = repository.get_by_email(db, user_in.email)
        if existing and existing.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Email '{user_in.email}' già assegnata a un altro utente",
            )

    user = repository.update(db, user_id, user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Utente con id {user_id} non trovato",
        )
    return user


def delete_user(db: Session, user_id: int) -> None:
    """Elimina un utente per ID.

    Solleva HTTPException 404 se non trovato.
    """
    deleted = repository.delete(db, user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Utente con id {user_id} non trovato",
        )

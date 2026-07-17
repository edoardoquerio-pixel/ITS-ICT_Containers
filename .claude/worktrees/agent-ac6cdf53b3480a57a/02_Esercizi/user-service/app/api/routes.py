"""Route REST per il User Service."""

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import User, UserCreate, UserUpdate
from app.services import service as user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[User])
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    """Restituisce l'elenco degli utenti."""
    return user_service.get_users(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Restituisce un utente specifico per ID."""
    return user_service.get_user(db, user_id)


@router.post("", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """Crea un nuovo utente. 409 se email duplicata."""
    return user_service.create_user(db, user_in)


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    """Aggiorna un utente. 404 se non trovato, 409 se email duplicata."""
    return user_service.update_user(db, user_id, user_in)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Elimina un utente. 404 se non trovato."""
    user_service.delete_user(db, user_id)

"""Schemi Pydantic per la validazione e serializzazione dei dati User."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """Campi comuni a tutte le operazioni."""
    name: str = Field(..., min_length=1, max_length=255)
    email: str = Field(..., max_length=255)


class UserCreate(UserBase):
    """Usato per la creazione (POST)."""
    pass


class UserUpdate(BaseModel):
    """Usato per aggiornamento parziale. Tutti i campi opzionali."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    email: Optional[str] = Field(None, max_length=255)


class User(UserBase):
    """Modello completo con id e timestamp, usato per le response."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

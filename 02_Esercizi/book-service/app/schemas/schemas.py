"""Schemi Pydantic per la validazione e serializzazione dei dati Book.

Separazione in classi base/create/update per seguire le best practice REST.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class BookBase(BaseModel):
    """Campi comuni a tutte le operazioni."""
    titolo: str = Field(..., min_length=1, max_length=255)
    autore: str = Field(..., min_length=1, max_length=255)
    isbn: str = Field(..., min_length=10, max_length=20)
    anno_pubblicazione: Optional[int] = Field(None, ge=1400, le=2100)
    genere: Optional[str] = Field(None, max_length=100)
    disponibile: bool = True


class BookCreate(BookBase):
    """Usato per la creazione (POST)."""
    pass


class BookUpdate(BaseModel):
    """Usato per aggiornamento parziale. Tutti i campi opzionali."""
    titolo: Optional[str] = Field(None, min_length=1, max_length=255)
    autore: Optional[str] = Field(None, min_length=1, max_length=255)
    isbn: Optional[str] = Field(None, min_length=10, max_length=20)
    anno_pubblicazione: Optional[int] = Field(None, ge=1400, le=2100)
    genere: Optional[str] = Field(None, max_length=100)
    disponibile: Optional[bool] = None


class Book(BookBase):
    """Modello completo con id e timestamp, usato per le response."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

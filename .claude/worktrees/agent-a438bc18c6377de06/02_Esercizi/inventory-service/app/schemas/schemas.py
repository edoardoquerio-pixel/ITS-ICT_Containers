"""Schemi Pydantic per la validazione e serializzazione dei dati Stock."""

from datetime import datetime

from pydantic import BaseModel, Field


class StockBase(BaseModel):
    """Campi comuni per le operazioni sulle scorte."""
    book_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=0)


class StockCreate(StockBase):
    """Usato per la creazione (POST)."""
    pass


class StockEntry(StockBase):
    """Modello completo con id e timestamp, usato per le response."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

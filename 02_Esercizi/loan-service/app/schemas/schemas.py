"""Schemi Pydantic per la validazione e serializzazione dei dati Loan."""

from datetime import datetime

from pydantic import BaseModel, Field


class LoanBase(BaseModel):
    """Campi comuni a tutte le operazioni."""
    user_id: int = Field(..., gt=0)
    book_id: int = Field(..., gt=0)


class LoanCreate(LoanBase):
    """Usato per la creazione (POST)."""
    pass


class Loan(LoanBase):
    """Modello completo con id e timestamp, usato per le response."""
    id: int
    active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

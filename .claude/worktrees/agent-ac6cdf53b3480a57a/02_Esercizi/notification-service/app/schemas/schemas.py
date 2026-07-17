"""Schemi Pydantic per la validazione e serializzazione dei dati Notification."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NotificationBase(BaseModel):
    """Campi comuni per le operazioni sulle notifiche."""
    user_id: int = Field(..., gt=0)
    channel: str = Field(default="email", max_length=50)
    message: str = Field(..., min_length=1)


class NotificationCreate(NotificationBase):
    """Usato per la creazione (POST)."""
    pass


class Notification(NotificationBase):
    """Modello completo con id, status e timestamp, usato per le response."""
    id: int
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}

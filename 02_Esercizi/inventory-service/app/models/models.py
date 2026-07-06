"""Modello ORM Inventory per SQLAlchemy."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer

from app.database.database import Base


class InventoryORM(Base):
    """Modello SQLAlchemy per la tabella inventory."""

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, nullable=False, unique=True)
    quantity = Column(Integer, nullable=False, default=0)
    created_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

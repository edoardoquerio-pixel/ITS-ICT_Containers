"""Modello ORM Book per SQLAlchemy.

Rappresenta la tabella 'books' nel database.
"""
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.database.database import Base


class BookORM(Base):
    """Modello SQLAlchemy per la tabella books."""

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titolo = Column(String(255), nullable=False)
    autore = Column(String(255), nullable=False)
    isbn = Column(String(20), nullable=False, unique=True)
    anno_pubblicazione = Column(Integer, nullable=True)
    genere = Column(String(100), nullable=True)
    disponibile = Column(Boolean, nullable=False, default=True)
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

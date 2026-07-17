"""Modello ORM Loan per SQLAlchemy."""

from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Integer

from app.database.database import Base


class LoanORM(Base):
    """Modello SQLAlchemy per la tabella loans."""

    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
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

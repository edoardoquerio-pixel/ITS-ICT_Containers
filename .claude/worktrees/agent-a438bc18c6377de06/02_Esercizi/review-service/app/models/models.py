"""Modello ORM Review per SQLAlchemy."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String

from app.database.database import Base


class ReviewORM(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(500), nullable=True)
    created_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

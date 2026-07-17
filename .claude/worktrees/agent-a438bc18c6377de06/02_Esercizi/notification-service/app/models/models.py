"""Modello ORM Notification per SQLAlchemy."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database.database import Base


class NotificationORM(Base):
    """Modello SQLAlchemy per la tabella notifications."""

    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    channel = Column(String(50), nullable=False, default="email")
    message = Column(Text, nullable=False)
    status = Column(String(50), nullable=False, default="sent")
    created_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

"""Repository per l'entità Notification.

Fornisce metodi CRUD usando SQLAlchemy ORM.
"""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import NotificationORM
from app.schemas.schemas import Notification, NotificationCreate


def _orm_to_schema(orm: NotificationORM) -> Notification:
    """Converte un modello ORM in schema Pydantic."""
    return Notification(
        id=orm.id,
        user_id=orm.user_id,
        channel=orm.channel,
        message=orm.message,
        status=orm.status,
        created_at=orm.created_at,
    )


def create(db: Session, notif_in: NotificationCreate) -> Notification:
    """Inserisce una nuova notifica e restituisce il record completo."""
    orm = NotificationORM(
        user_id=notif_in.user_id,
        channel=notif_in.channel,
        message=notif_in.message,
        status="sent",
    )
    db.add(orm)
    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)


def get_all(db: Session) -> list[Notification]:
    """Restituisce tutte le notifiche, ordinate dalla più recente."""
    stmt = select(NotificationORM).order_by(NotificationORM.created_at.desc())
    orms = db.execute(stmt).scalars().all()
    return [_orm_to_schema(o) for o in orms]

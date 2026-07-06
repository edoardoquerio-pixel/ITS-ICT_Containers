"""Service layer per le Notification.

Contiene la logica di business e coordina le operazioni
tra api e repository. Usa SQLAlchemy session.
"""
import logging

from sqlalchemy.orm import Session

from app.repositories import repository
from app.schemas.schemas import Notification, NotificationCreate

logger = logging.getLogger(__name__)


def send_notification(db: Session, notif_in: NotificationCreate) -> Notification:
    """Invia (salva) una notifica."""
    entry = repository.create(db, notif_in)
    logger.info(
        "Notification sent to user %d via %s: %s",
        notif_in.user_id,
        notif_in.channel,
        notif_in.message[:50],
    )
    return entry


def get_notifications(db: Session) -> list[Notification]:
    """Restituisce tutte le notifiche."""
    return repository.get_all(db)

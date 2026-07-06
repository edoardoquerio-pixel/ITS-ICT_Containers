"""Route REST per il Notification Service."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import Notification, NotificationCreate
from app.services import service as notification_service

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("", response_model=list[Notification])
def list_notifications(db: Session = Depends(get_db)):
    """Restituisce l'elenco delle notifiche."""
    return notification_service.get_notifications(db)


@router.post("", response_model=Notification, status_code=status.HTTP_201_CREATED)
def send_notification(notif_in: NotificationCreate, db: Session = Depends(get_db)):
    """Invia una nuova notifica."""
    return notification_service.send_notification(db, notif_in)

"""HTTP client per comunicazione inter-servizio (loan-service)."""
import httpx
from app.config import settings


async def check_book_exists(book_id: int) -> bool:
    """Verifica che un libro esista e sia disponibile in book-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.get(f"{settings.BOOK_SERVICE_URL}/books/{book_id}")
            if resp.status_code == 200:
                data = resp.json()
                return data.get("disponibile", False)
            return False
        except httpx.RequestError:
            return False


async def set_book_availability(book_id: int, disponibile: bool) -> bool:
    """Aggiorna la disponibilita di un libro in book-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.put(
                f"{settings.BOOK_SERVICE_URL}/books/{book_id}",
                json={"disponibile": disponibile},
            )
            return resp.status_code == 200
        except httpx.RequestError:
            return False


async def check_inventory(book_id: int, quantity: int = 1) -> bool:
    """Verifica che ci sia stock sufficiente in inventory-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.get(f"{settings.INVENTORY_SERVICE_URL}/inventory/{book_id}")
            if resp.status_code == 200:
                data = resp.json()
                return data.get("quantity", 0) >= quantity
            return True  # Se inventory non ha il book_id, permetti comunque
        except httpx.RequestError:
            return True  # Se inventory non risponde, permetti comunque


async def send_notification(user_id: int, channel: str, message: str) -> None:
    """Invia una notifica a notification-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            await client.post(
                f"{settings.NOTIFICATION_SERVICE_URL}/notifications",
                json={"user_id": user_id, "channel": channel, "message": message},
            )
        except httpx.RequestError:
            pass  # Non bloccare il flusso principale se notifica fallisce

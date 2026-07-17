"""HTTP client per comunicazione inter-servizio (review-service)."""
import httpx
from app.config import settings


async def check_book_exists(book_id: int) -> bool:
    """Verifica che un libro esista in book-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.get(f"{settings.BOOK_SERVICE_URL}/books/{book_id}")
            return resp.status_code == 200
        except httpx.RequestError:
            return False

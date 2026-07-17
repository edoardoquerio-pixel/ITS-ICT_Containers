"""Route REST per il Inventory Service."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import StockCreate, StockEntry
from app.services import service as inventory_service

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("", response_model=list[StockEntry])
def list_inventory(db: Session = Depends(get_db)):
    """Restituisce l'elenco delle scorte."""
    return inventory_service.get_all_stock(db)


@router.get("/{book_id}", response_model=StockEntry)
def get_stock(book_id: int, db: Session = Depends(get_db)):
    """Restituisce le scorte per un libro. 404 se non trovato."""
    return inventory_service.get_stock(db, book_id)


@router.post("", response_model=StockEntry, status_code=status.HTTP_201_CREATED)
def set_stock(stock_in: StockCreate, db: Session = Depends(get_db)):
    """Crea o aggiorna le scorte per un libro."""
    return inventory_service.set_stock(db, stock_in)

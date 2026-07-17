"""Route REST per il Loan Service."""

from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import Loan, LoanCreate
from app.services import service as loan_service

router = APIRouter(prefix="/loans", tags=["loans"])


@router.get("", response_model=list[Loan])
def list_loans(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    active_only: Optional[bool] = Query(None),
    db: Session = Depends(get_db),
):
    """Restituisce l'elenco dei prestiti."""
    return loan_service.get_loans(db, skip=skip, limit=limit, active_only=active_only)


@router.get("/{loan_id}", response_model=Loan)
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    """Restituisce un prestito specifico per ID."""
    return loan_service.get_loan(db, loan_id)


@router.post("", response_model=Loan, status_code=status.HTTP_201_CREATED)
def create_loan(loan_in: LoanCreate, db: Session = Depends(get_db)):
    """Crea un nuovo prestito."""
    return loan_service.create_loan(db, loan_in)


@router.put("/{loan_id}/return", response_model=Loan)
def return_loan(loan_id: int, db: Session = Depends(get_db)):
    """Registra la restituzione di un prestito. 404 se non trovato."""
    return loan_service.return_loan(db, loan_id)

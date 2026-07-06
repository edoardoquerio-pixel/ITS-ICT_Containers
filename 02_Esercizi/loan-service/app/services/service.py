"""Service layer per il Loan."""
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import repository
from app.schemas.schemas import Loan, LoanCreate


def create_loan(db: Session, loan_in: LoanCreate) -> Loan:
    return repository.create(db, loan_in)


def get_loan(db: Session, loan_id: int) -> Loan:
    loan = repository.get_by_id(db, loan_id)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prestito con id {loan_id} non trovato",
        )
    return loan


def get_loans(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    active_only: Optional[bool] = None,
) -> list[Loan]:
    return repository.get_all(db, skip=skip, limit=limit, active_only=active_only)


def return_loan(db: Session, loan_id: int) -> Loan:
    loan = repository.return_loan(db, loan_id)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prestito con id {loan_id} non trovato",
        )
    return loan

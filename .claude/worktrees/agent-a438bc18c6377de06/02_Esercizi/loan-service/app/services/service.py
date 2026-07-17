"""Service layer per il Loan."""
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import repository
from app.schemas.schemas import Loan, LoanCreate
from app.services.client import (
    check_book_exists,
    check_inventory,
    set_book_availability,
    send_notification,
)


async def create_loan_async(db: Session, loan_in: LoanCreate) -> Loan:
    """Crea un prestito dopo aver verificato disponibilita e stock."""
    # 1. Verifica che il libro esista e sia disponibile
    available = await check_book_exists(loan_in.book_id)
    if not available:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Libro non disponibile per il prestito",
        )

    # 2. Verifica stock
    has_stock = await check_inventory(loan_in.book_id)
    if not has_stock:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Scorte insufficienti per il prestito",
        )

    # 3. Crea prestito
    loan = repository.create(db, loan_in)

    # 4. Aggiorna disponibilita libro
    await set_book_availability(loan_in.book_id, False)

    # 5. Invia notifica
    await send_notification(
        user_id=loan_in.user_id,
        channel="email",
        message=f"Prestito effettuato per libro ID {loan_in.book_id}",
    )

    return loan


async def return_loan_async(db: Session, loan_id: int) -> Loan:
    """Restituisce un prestito e riabilita la disponibilita del libro."""
    loan = repository.return_loan(db, loan_id)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prestito con id {loan_id} non trovato",
        )
    # Riabilita disponibilita libro
    await set_book_availability(loan.book_id, True)
    # Notifica
    await send_notification(
        user_id=loan.user_id,
        channel="email",
        message=f"Restituzione completata per libro ID {loan.book_id}",
    )
    return loan


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

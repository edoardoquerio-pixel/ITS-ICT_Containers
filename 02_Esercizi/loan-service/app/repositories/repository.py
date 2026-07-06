"""Repository per l'entità Loan."""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import LoanORM
from app.schemas.schemas import Loan, LoanCreate


def _orm_to_schema(orm: LoanORM) -> Loan:
    return Loan(
        id=orm.id,
        user_id=orm.user_id,
        book_id=orm.book_id,
        active=orm.active,
        created_at=orm.created_at,
        updated_at=orm.updated_at,
    )


def create(db: Session, loan_in: LoanCreate) -> Loan:
    orm = LoanORM(
        user_id=loan_in.user_id,
        book_id=loan_in.book_id,
    )
    db.add(orm)
    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)


def get_by_id(db: Session, loan_id: int) -> Optional[Loan]:
    orm = db.get(LoanORM, loan_id)
    return _orm_to_schema(orm) if orm else None


def get_all(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    active_only: Optional[bool] = None,
) -> list[Loan]:
    stmt = select(LoanORM)

    if active_only is not None:
        stmt = stmt.where(LoanORM.active == active_only)

    stmt = stmt.order_by(LoanORM.created_at.desc()).offset(skip).limit(limit)
    orms = db.execute(stmt).scalars().all()
    return [_orm_to_schema(o) for o in orms]


def return_loan(db: Session, loan_id: int) -> Optional[Loan]:
    orm = db.get(LoanORM, loan_id)
    if not orm:
        return None
    orm.active = False
    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)

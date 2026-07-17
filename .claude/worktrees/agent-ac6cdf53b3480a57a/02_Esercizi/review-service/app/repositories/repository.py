"""Repository per l'entità Review."""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import ReviewORM
from app.schemas.schemas import Review, ReviewCreate


def _orm_to_schema(orm: ReviewORM) -> Review:
    return Review(
        id=orm.id,
        book_id=orm.book_id,
        user_id=orm.user_id,
        rating=orm.rating,
        comment=orm.comment,
        created_at=orm.created_at,
    )


def create(db: Session, review_in: ReviewCreate) -> Review:
    orm = ReviewORM(
        book_id=review_in.book_id,
        user_id=review_in.user_id,
        rating=review_in.rating,
        comment=review_in.comment,
    )
    db.add(orm)
    db.commit()
    db.refresh(orm)
    return _orm_to_schema(orm)


def get_by_id(db: Session, review_id: int) -> Optional[Review]:
    orm = db.get(ReviewORM, review_id)
    return _orm_to_schema(orm) if orm else None


def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[Review]:
    stmt = select(ReviewORM).order_by(ReviewORM.created_at.desc()).offset(skip).limit(limit)
    orms = db.execute(stmt).scalars().all()
    return [_orm_to_schema(o) for o in orms]


def get_by_book(db: Session, book_id: int) -> list[Review]:
    stmt = select(ReviewORM).where(ReviewORM.book_id == book_id).order_by(ReviewORM.created_at.desc())
    orms = db.execute(stmt).scalars().all()
    return [_orm_to_schema(o) for o in orms]

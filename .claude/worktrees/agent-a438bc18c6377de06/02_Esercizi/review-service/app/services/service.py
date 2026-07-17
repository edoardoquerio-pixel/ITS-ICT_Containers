"""Service layer per la Review."""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import repository
from app.schemas.schemas import Review, ReviewCreate


def create_review(db: Session, review_in: ReviewCreate) -> Review:
    return repository.create(db, review_in)


def get_review(db: Session, review_id: int) -> Review:
    review = repository.get_by_id(db, review_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recensione con id {review_id} non trovata",
        )
    return review


def get_reviews(db: Session, skip: int = 0, limit: int = 100) -> list[Review]:
    return repository.get_all(db, skip=skip, limit=limit)


def get_reviews_by_book(db: Session, book_id: int) -> list[Review]:
    return repository.get_by_book(db, book_id)

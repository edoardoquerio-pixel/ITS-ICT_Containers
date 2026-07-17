"""Service layer per la Review."""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import repository
from app.schemas.schemas import Review, ReviewCreate
from app.services.client import check_book_exists


async def create_review_async(db: Session, review_in: ReviewCreate) -> Review:
    """Crea una recensione dopo aver verificato che il libro esista."""
    exists = await check_book_exists(review_in.book_id)
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Il libro specificato non esiste",
        )
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

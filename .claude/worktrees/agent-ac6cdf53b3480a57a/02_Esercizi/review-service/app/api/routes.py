"""Route REST per il Review Service."""

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import Review, ReviewCreate
from app.services import service as review_service

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.get("", response_model=list[Review])
def list_reviews(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return review_service.get_reviews(db, skip=skip, limit=limit)


@router.get("/by-book/{book_id}", response_model=list[Review])
def get_reviews_by_book(book_id: int, db: Session = Depends(get_db)):
    return review_service.get_reviews_by_book(db, book_id)


@router.get("/{review_id}", response_model=Review)
def get_review(review_id: int, db: Session = Depends(get_db)):
    return review_service.get_review(db, review_id)


@router.post("", response_model=Review, status_code=status.HTTP_201_CREATED)
async def create_review(review_in: ReviewCreate, db: Session = Depends(get_db)):
    return await review_service.create_review_async(db, review_in)

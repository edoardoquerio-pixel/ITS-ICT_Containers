"""Schemi Pydantic per Review."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReviewBase(BaseModel):
    book_id: int = Field(..., gt=0)
    user_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=500)


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}

from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    year: int
    id_author: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None
    id_author: Optional[int] = None

class BookResponse(BaseModel):
    id_book: int
    title: str
    year: int
    id_author: int

    class Config:
        from_attributes = True

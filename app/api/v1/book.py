# app/api/v1/book.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.services.book_service import BookService
from app.api.dependecies import get_db

router = APIRouter()

@router.post("/", response_model=BookResponse)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    return BookService.create(db, data)

@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return BookService.get_all(db)

@router.get("/{id_book}", response_model=BookResponse)
def get_book(id_book: int, db: Session = Depends(get_db)):
    book = BookService.get_by_id(db, id_book)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@router.put("/{id_book}", response_model=BookResponse)
def update_book(id_book: int, data: BookUpdate, db: Session = Depends(get_db)):
    book = BookService.update(db, id_book, data)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@router.delete("/{id_book}")
def delete_book(id_book: int, db: Session = Depends(get_db)):
    success = BookService.delete(db, id_book)

    if not success:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted successfully"}

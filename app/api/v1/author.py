# app/api/v1/author.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.author import AuthorCreate, AuthorResponse, AuthorUpdate
from app.services.author_service import AuthorService
from app.api.dependecies import get_db

router = APIRouter()

@router.post("/", response_model=AuthorResponse)
def create_author(data: AuthorCreate, db: Session = Depends(get_db)):
    return AuthorService.create(db, data)

@router.get("/", response_model=list[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return AuthorService.get_all(db)

@router.get("/{id_author}", response_model=AuthorResponse)
def get_author(id_author: int, db: Session = Depends(get_db)):
    author = AuthorService.get_by_id(db, id_author)

    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return author

@router.put("/{id_author}", response_model=AuthorResponse)
def update_author(id_author: int, data: AuthorUpdate, db: Session = Depends(get_db)):
    author = AuthorService.update(db, id_author, data)

    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return author

@router.delete("/{id_author}")
def delete_author(id_author: int, db: Session = Depends(get_db)):
    success = AuthorService.delete(db, id_author)

    if not success:
        raise HTTPException(status_code=404, detail="Author not found")

    return {"message": "Author deleted successfully"}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.services.book_service import BookService
from app.api.dependecies import get_db, get_mongo, get_redis
from app.db.mongo.mongo_client import MongoClientManager
from app.db.redis.redis_client import RedisClient
router = APIRouter()

@router.post("/", response_model=BookResponse)
def create_book(
    data: BookCreate, 
    db: Session = Depends(get_db),
    redis: RedisClient = Depends(get_redis),
    mongo: MongoClientManager = Depends(get_mongo)
):
    return BookService(redis, mongo).create(db, data)

@router.get("/", response_model=list[BookResponse])
def get_books(
    db: Session = Depends(get_db),
    redis: RedisClient = Depends(get_redis),
    mongo: MongoClientManager = Depends(get_mongo)
):
    return BookService(redis, mongo).get_all(db)

@router.get("/{id_book}", response_model=BookResponse)
def get_book(
    id_book: int, 
    db: Session = Depends(get_db),
    redis: RedisClient = Depends(get_redis),
    mongo: MongoClientManager = Depends(get_mongo)
):
    book = BookService(redis, mongo).get_by_id(db, id_book)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@router.put("/{id_book}", response_model=BookResponse)
def update_book(
    id_book: int, 
    data: BookUpdate, 
    db: Session = Depends(get_db),
    redis: RedisClient = Depends(get_redis),
    mongo: MongoClientManager = Depends(get_mongo)
):
    book = BookService(redis, mongo).update(db, id_book, data)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@router.delete("/{id_book}")
def delete_book(
    id_book: int, 
    db: Session = Depends(get_db),
    redis: RedisClient = Depends(get_redis),
    mongo: MongoClientManager = Depends(get_mongo)
):
    success = BookService(redis, mongo).delete(db, id_book)

    if not success:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted successfully"}

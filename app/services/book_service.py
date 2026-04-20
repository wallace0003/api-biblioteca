from sqlalchemy.orm import Session
from app.models import Book
from app.schemas.book import BookCreate, BookUpdate
from app.db.redis.redis_client import RedisClient
import os
from dotenv import load_dotenv

#TODO: iniciarlizar redis no dependecies. Passar como parâmetro no construtor de "BookService"
load_dotenv()
redis_client = RedisClient(
    host=os.getenv("redis_host"),
    port=int(os.getenv("redis_port")),
    db=int(os.getenv("redis_n_db"))
)


class BookService:
    @staticmethod
    def _to_dict_list(books):
        return [
            {
                "id_book": b.id_book,
                "title": b.title,
                "year": b.year,
                "id_author": b.id_author
            }
            for b in books
        ]

    @staticmethod
    def create(db: Session, data: BookCreate):
        book = Book(**data.model_dump())

        db.add(book)
        db.commit()
        db.refresh(book)
        books = db.query(Book).all()
        books_dict = BookService._to_dict_list(books)

        redis_client.set_books(books_dict)

        return book

    @staticmethod
    def get_all(db: Session):
        cached = redis_client.get_books()
        if cached:
            print("Get Redis")
            return cached

        print("Get PostgreSQL")

        books = db.query(Book).all()
        books_dict = BookService._to_dict_list(books)
        redis_client.set_books(books_dict)

        return books_dict

    @staticmethod
    def get_by_id(db: Session, id_book: int):
        return db.query(Book).filter(Book.id_book == id_book).first()

    @staticmethod
    def update(db: Session, id_book: int, data: BookUpdate):
        book = db.query(Book).filter(Book.id_book == id_book).first()

        if not book:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(book, key, value)

        db.commit()
        db.refresh(book)

        books = db.query(Book).all()
        books_dict = BookService._to_dict_list(books)
        redis_client.set_books(books_dict)

        return book

    @staticmethod
    def delete(db: Session, id_book: int):
        book = db.query(Book).filter(Book.id_book == id_book).first()

        if not book:
            return False

        db.delete(book)
        db.commit()

        books = db.query(Book).all()
        books_dict = BookService._to_dict_list(books)
        redis_client.set_books(books_dict)

        return True

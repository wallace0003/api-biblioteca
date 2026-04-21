from sqlalchemy.orm import Session
from app.models import Book
from app.schemas.book import BookCreate, BookUpdate
from app.db.redis.redis_client import RedisClient
from app.db.mongo.mongo_client import MongoClientManager


class BookService:
    def __init__(self, redis: RedisClient, mongo: MongoClientManager):
        self.redis = redis
        self.mongo = mongo

    def _to_dict_list(self, books):
        return [
            {
                "id_book": b.id_book,
                "title": b.title,
                "year": b.year,
                "id_author": b.id_author
            }
            for b in books
        ]

    def create(self, db: Session, data: BookCreate):
        book = Book(**data.model_dump())

        db.add(book)
        db.commit()
        db.refresh(book)

        books = db.query(Book).all()
        books_dict = self._to_dict_list(books)
        self.redis.set_books(books_dict)

        try:
            self.mongo.insert_log("logs", {
                "event": "CREATE_BOOK",
                "book_id": book.id_book,
                "data": data.model_dump()
            })
        except Exception:
            pass

        return book

    def get_all(self, db: Session):
        cached = self.redis.get_books()

        if cached:
            print("get with Redis")

            try:
                self.mongo.insert_log("logs", {
                    "event": "GET_ALL_BOOKS",
                    "source": "redis"
                })
            except:
                pass

            return cached

        print("get with PostgreSQL")

        books = db.query(Book).all()
        books_dict = self._to_dict_list(books)

        self.redis.set_books(books_dict)

        try:
            self.mongo.insert_log("logs", {
                "event": "GET_ALL_BOOKS",
                "source": "database",
                "count": len(books_dict)
            })
        except:
            pass

        return books_dict

    def get_by_id(self, db: Session, id_book: int):
        book = db.query(Book).filter(Book.id_book == id_book).first()

        try:
            self.mongo.insert_log("logs", {
                "event": "GET_BOOK",
                "book_id": id_book,
                "found": bool(book)
            })
        except:
            pass

        return book

    def update(self, db: Session, id_book: int, data: BookUpdate):
        book = db.query(Book).filter(Book.id_book == id_book).first()

        if not book:
            try:
                self.mongo.insert_log("logs", {
                    "event": "UPDATE_BOOK",
                    "book_id": id_book,
                    "status": "NOT_FOUND"
                })
            except:
                pass
            return None

        old_data = {
            "title": book.title,
            "year": book.year
        }

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(book, key, value)

        db.commit()
        db.refresh(book)

        books = db.query(Book).all()
        books_dict = self._to_dict_list(books)
        self.redis.set_books(books_dict)

        try:
            self.mongo.insert_log("logs", {
                "event": "UPDATE_BOOK",
                "book_id": id_book,
                "old_data": old_data,
                "new_data": data.model_dump(exclude_unset=True)
            })
        except:
            pass

        return book

    def delete(self, db: Session, id_book: int):
        book = db.query(Book).filter(Book.id_book == id_book).first()

        if not book:
            try:
                self.mongo.insert_log("logs", {
                    "event": "DELETE_BOOK",
                    "book_id": id_book,
                    "status": "NOT_FOUND"
                })
            except:
                pass
            return False

        db.delete(book)
        db.commit()

        books = db.query(Book).all()
        books_dict = self._to_dict_list(books)
        self.redis.set_books(books_dict)

        try:
            self.mongo.insert_log("logs", {
                "event": "DELETE_BOOK",
                "book_id": id_book,
                "status": "SUCCESS"
            })
        except:
            pass

        return True

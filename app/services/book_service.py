from sqlalchemy.orm import Session
from app.models import Book
from app.schemas.book import BookCreate, BookUpdate

class BookService:

    @staticmethod
    def create(db: Session, data: BookCreate):
        book = Book(**data.model_dump())
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    @staticmethod
    def get_all(db: Session):
        return db.query(Book).all()

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
        return book

    @staticmethod
    def delete(db: Session, id_book: int):
        book = db.query(Book).filter(Book.id_book == id_book).first()

        if not book:
            return False

        db.delete(book)
        db.commit()
        return True

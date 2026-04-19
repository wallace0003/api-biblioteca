from sqlalchemy.orm import Session
from app.models import Author
from app.schemas.author import AuthorCreate, AuthorUpdate

class AuthorService:

    @staticmethod
    def create(db: Session, data: AuthorCreate):
        author = Author(**data.model_dump())
        db.add(author)
        db.commit()
        db.refresh(author)
        return author

    @staticmethod
    def get_all(db: Session):
        return db.query(Author).all()

    @staticmethod
    def get_by_id(db: Session, id_author: int):
        return db.query(Author).filter(Author.id_author == id_author).first()

    @staticmethod
    def update(db: Session, id_author: int, data: AuthorUpdate):
        author = db.query(Author).filter(Author.id_author == id_author).first()

        if not author:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(author, key, value)

        db.commit()
        db.refresh(author)
        return author

    @staticmethod
    def delete(db: Session, id_author: int):
        author = db.query(Author).filter(Author.id_author == id_author).first()

        if not author:
            return False

        db.delete(author)
        db.commit()
        return True

from sqlalchemy.orm import Session
from app.models import Author
from app.schemas.author import AuthorCreate, AuthorUpdate
from app.db.mongo.mongo_client import MongoClientManager
import os
from dotenv import load_dotenv

load_dotenv()

mongo = MongoClientManager(
    uri=os.getenv("mongo_uri"),
    database=os.getenv("mongo_db")
)


class AuthorService:

    @staticmethod
    def create(db: Session, data: AuthorCreate):
        author = Author(**data.model_dump())

        db.add(author)
        db.commit()
        db.refresh(author)

        mongo.insert_log("logs", {
            "event": "CREATE_AUTHOR",
            "author_id": author.id_author,
            "data": data.model_dump()
        })

        return author

    @staticmethod
    def get_all(db: Session):
        authors = db.query(Author).all()

        mongo.insert_log("logs", {
            "event": "GET_ALL_AUTHORS",
            "count": len(authors)
        })

        return authors

    @staticmethod
    def get_by_id(db: Session, id_author: int):
        author = db.query(Author).filter(Author.id_author == id_author).first()

        mongo.insert_log("logs", {
            "event": "GET_AUTHOR",
            "author_id": id_author,
            "found": bool(author)
        })

        return author

    @staticmethod
    def update(db: Session, id_author: int, data: AuthorUpdate):
        author = db.query(Author).filter(Author.id_author == id_author).first()

        if not author:
            mongo.insert_log("logs", {
                "event": "UPDATE_AUTHOR",
                "author_id": id_author,
                "status": "NOT_FOUND"
            })
            return None

        old_data = {
            "author_name": author.author_name
        }

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(author, key, value)

        db.commit()
        db.refresh(author)

        mongo.insert_log("logs", {
            "event": "UPDATE_AUTHOR",
            "author_id": id_author,
            "old_data": old_data,
            "new_data": data.model_dump(exclude_unset=True)
        })

        return author

    @staticmethod
    def delete(db: Session, id_author: int):
        author = db.query(Author).filter(Author.id_author == id_author).first()

        if not author:
            mongo.insert_log("logs", {
                "event": "DELETE_AUTHOR",
                "author_id": id_author,
                "status": "NOT_FOUND"
            })
            return False

        db.delete(author)
        db.commit()

        mongo.insert_log("logs", {
            "event": "DELETE_AUTHOR",
            "author_id": id_author,
            "status": "SUCCESS"
        })

        return True

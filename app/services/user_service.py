from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate, UserUpdate
from app.db.mongo.mongo_client import MongoClientManager


class UserService:
    def __init__(self, mongo: MongoClientManager):
        self.mongo = mongo

    def create_user(self, db: Session, user_data: UserCreate) -> User:
        user = User(**user_data.model_dump())

        db.add(user)
        db.commit()
        db.refresh(user)

        # 🔥 LOG
        try:
            self.mongo.insert_log("logs", {
                "event": "CREATE_USER",
                "user_id": user.id_user,
                "data": user_data.model_dump()
            })
        except:
            pass

        return user

    def get_all_users(self, db: Session):
        users = db.query(User).all()

        try:
            self.mongo.insert_log("logs", {
                "event": "GET_ALL_USERS",
                "count": len(users)
            })
        except:
            pass

        return users

    def get_user_by_id(self, db: Session, id_user: int):
        user = db.query(User).filter(User.id_user == id_user).first()

        try:
            self.mongo.insert_log("logs", {
                "event": "GET_USER",
                "user_id": id_user,
                "found": bool(user)
            })
        except:
            pass

        return user

    def update_user(self, db: Session, id_user: int, user_data: UserUpdate):
        user = db.query(User).filter(User.id_user == id_user).first()

        if not user:
            try:
                self.mongo.insert_log("logs", {
                    "event": "UPDATE_USER",
                    "user_id": id_user,
                    "status": "NOT_FOUND"
                })
            except:
                pass
            return None

        old_data = {
            "user_name": user.user_name,
            "email": user.email
        }

        for key, value in user_data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        try:
            self.mongo.insert_log("logs", {
                "event": "UPDATE_USER",
                "user_id": id_user,
                "old_data": old_data,
                "new_data": user_data.model_dump(exclude_unset=True)
            })
        except:
            pass

        return user

    def delete_user(self, db: Session, id_user: int):
        user = db.query(User).filter(User.id_user == id_user).first()

        if not user:
            try:
                self.mongo.insert_log("logs", {
                    "event": "DELETE_USER",
                    "user_id": id_user,
                    "status": "NOT_FOUND"
                })
            except:
                pass
            return False

        db.delete(user)
        db.commit()

        try:
            self.mongo.insert_log("logs", {
                "event": "DELETE_USER",
                "user_id": id_user,
                "status": "SUCCESS"
            })
        except:
            pass

        return True

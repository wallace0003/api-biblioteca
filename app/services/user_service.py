from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate, UserUpdate

class UserService:

    @staticmethod
    def create_user(
            db: Session, 
            user_data: UserCreate
        ) -> User:
        user = User(**user_data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_user_by_id(db: Session, id_user: int):
        return db.query(User).filter(User.id_user == id_user).first()

    @staticmethod
    def update_user(db: Session, id_user: int, user_data: UserUpdate):
        user = db.query(User).filter(User.id_user == id_user).first()

        if not user:
            return None

        for key, value in user_data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete_user(db: Session, id_user: int):
        user = db.query(User).filter(User.id_user == id_user).first()

        if not user:
            return False

        db.delete(user)
        db.commit()
        return True

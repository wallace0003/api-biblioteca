from fastapi import APIRouter, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService
from app.db.sql.engine import PostgresEngine
import os
from dotenv import load_dotenv

router = APIRouter()

def get_db():
    load_dotenv()
    database_url = os.getenv("database_url")
    db = PostgresEngine(database_url).get_session()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    try:
        return UserService.get_all_users(db)
    except Exception as e:
        print(e)
        return{
            "Failed": True
        }

@router.get("/{id_user}", response_model=UserResponse)
def get_user(id_user: int, db: Session = Depends(get_db)):
    user = UserService.get_user_by_id(db, id_user)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.put("/{id_user}", response_model=UserResponse)
def update_user(id_user: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = UserService.update_user(db, id_user, user_data)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.delete("/{id_user}")
def delete_user(id_user: int, db: Session = Depends(get_db)):
    success = UserService.delete_user(db, id_user)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}

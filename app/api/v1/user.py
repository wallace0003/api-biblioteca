from fastapi import APIRouter, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService
from app.api.dependecies import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return UserService.get_all_users(db)
    

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

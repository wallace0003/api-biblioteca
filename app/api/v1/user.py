from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService
from app.api.dependecies import get_db, get_mongo
from app.db.mongo.mongo_client import MongoClientManager

router = APIRouter()


def get_user_service(mongo: MongoClientManager = Depends(get_mongo)):
    return UserService(mongo)


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    return service.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    return service.get_all_users(db)


@router.get("/{id_user}", response_model=UserResponse)
def get_user(
    id_user: int,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    user = service.get_user_by_id(db, id_user)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.put("/{id_user}", response_model=UserResponse)
def update_user(
    id_user: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    user = service.update_user(db, id_user, user_data)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.delete("/{id_user}")
def delete_user(
    id_user: int,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    success = service.delete_user(db, id_user)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}

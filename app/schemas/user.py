from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    user_name: str
    email: EmailStr

class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    email: Optional[EmailStr] = None

class UserResponse(BaseModel):
    id_user: int
    user_name: str
    email: EmailStr

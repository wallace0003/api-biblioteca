from pydantic import BaseModel
from typing import Optional

class AuthorCreate(BaseModel):
    author_name: str

class AuthorUpdate(BaseModel):
    author_name: Optional[str] = None

class AuthorResponse(BaseModel):
    id_author: int
    author_name: str

    class Config:
        from_attributes = True

from pydantic import BaseModel, EmailStr
from typing import Optional

# É uma boa prática nunca usar o mesmo schema para entrada e saída.
class CreateUser(BaseModel):
    id:int
    name: str
    email: EmailStr
    age: Optional[int]
    password:str

class ResponseUser(BaseModel):
    sucess:bool
    name:str
    age: Optional[int]

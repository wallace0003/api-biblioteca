from fastapi import  APIRouter, status
from app.schemas.user import CreateUser, ResponseUser

#TODO: Lógica para adicionar usuário
router = APIRouter()

@router.post(
    "",
    response_model=ResponseUser,
    status_code=status.HTTP_201_CREATED
)
async def createUser(user:CreateUser):
    return ResponseUser(
        id=1,
        name=user.name,
        age=user.age,
        sucess=True
    )

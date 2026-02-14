# app/api/routes/example.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def ping():
    return {"ping": "pong"}

@router.post("/teste_post")
async def manda_post():
    return{"post é?": "sim sim"}

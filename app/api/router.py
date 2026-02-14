# app/api/router.py
from fastapi import APIRouter
from app.api.v1 import example

api_router = APIRouter(prefix="/api")

api_router.include_router(
    example.router,
    prefix="/example",
    tags=["Example"]
)

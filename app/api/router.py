# app/api/router.py
from fastapi import APIRouter
from app.api.v1 import example, user, loan, author, book, log

api_router = APIRouter(prefix="/api")

api_router.include_router(
    user.router,
    prefix="/users",
    tags=["User"]
)


api_router.include_router(
    loan.router,
    prefix="/loans",
    tags=["loans"]
)


api_router.include_router(
    author.router,
    prefix="/authors",
    tags=["authors"]
)


api_router.include_router(
    book.router,
    prefix="/books",
    tags=["books"]
)

api_router.include_router(
    log.router,
    prefix="/logs",
    tags=["logs"]
)

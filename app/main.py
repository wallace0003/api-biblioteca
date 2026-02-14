# app/main.py
from fastapi import FastAPI
from app.api.router import api_router
import uvicorn

app = FastAPI(
    title="Testando chamada da API.",
    version="0.0.0"
)

app.include_router(api_router)

@app.get("/")
async def teste():
    return {"status": "API rodando"}

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

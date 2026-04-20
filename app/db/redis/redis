import redis
import json
from typing import List, Optional

class RedisClient:
    def __init__(self, host:str, port:int, db:int):
        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True 
        )

    def set_books(self, books: List[dict], ttl: int = 300):
        self.client.set(
            "books:all",
            json.dumps(books),
            ex=ttl
        )

    def get_books(self) -> Optional[List[dict]]:
        data = self.client.get("books:all")

        if data:
            return json.loads(data)

        return None

    def invalidate_books(self):
        self.client.delete("books:all")

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    redis_client = RedisClient(
        host=os.getenv("redis_host"),
        port=int(os.getenv("redis_port")),
        db=int(os.getenv("redis_n_db"))
    )

    books = [
        {"id_book": 1, "title": "1984", "year": 1949},
        {"id_book": 2, "title": "Animal Farm", "year": 1945}
    ]

    redis_client.set_books(books)
    print("✅ Dados salvos no Redis")

    cached_books = redis_client.get_books()
    print("📦 Dados do Redis:", cached_books)

    redis_client.invalidate_books()
    
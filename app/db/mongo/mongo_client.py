from pymongo import MongoClient
from typing import Optional, List, Dict, Any
from datetime import datetime


class MongoClientManager:
    def __init__(self, uri: str, database: str):
        self.client = MongoClient(uri)
        self.db = self.client[database]

    def insert_log(self, collection: str, data: Dict[str, Any]):
        document = {
            **data,
            "created_at": datetime.now()
        }

        result = self.db[collection].insert_one(document)
        return str(result.inserted_id)

    def insert_many_logs(self, collection: str, data: List[Dict[str, Any]]):
        documents = [
            {**d, "created_at": datetime.now()}
            for d in data
        ]

        result = self.db[collection].insert_many(documents)
        return [str(_id) for _id in result.inserted_ids]

    def find_logs(
        self,
        collection: str,
        query: Optional[Dict[str, Any]] = None,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        query = query or {}

        cursor = self.db[collection].find(query).limit(limit)

        return [
            {**doc, "_id": str(doc["_id"])}
            for doc in cursor
        ]

    def delete_logs(self, collection: str, query: Dict[str, Any]):
        result = self.db[collection].delete_many(query)
        return result.deleted_count

    def clear_collection(self, collection: str):
        self.db[collection].delete_many({})

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    mongo = MongoClientManager(
        uri=os.getenv("mongo_uri"),
        database=os.getenv("mongo_db")
    )

    log = {
        "event": "CREATE_BOOK",
        "user": "Wallace",
        "payload": {
            "title": "1984"
        }
    }

    mongo.insert_log("logs", log)
    print("✅ Log inserido")

    complex_log = {
        "event": "ERROR",
        "service": "book_service",
        "error": {
            "type": "IntegrityError",
            "message": "duplicate key"
        },
        "meta": {
            "ip": "127.0.0.1",
            "headers": {
                "user-agent": "Mozilla"
            }
        }
    }

    mongo.insert_log("logs", complex_log)
    print("🔥 Log complexo inserido")

    logs = mongo.find_logs("logs")
    print("📦 Logs:", logs)

    deleted = mongo.delete_logs("logs", {"event": "ERROR"})
    print(f"🗑️ Logs deletados: {deleted}")

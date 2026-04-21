from app.db.mongo.mongo_client import MongoClientManager
from typing import List, Optional
from bson import ObjectId


class LogService:

    def __init__(self, mongo: MongoClientManager):
        self.mongo = mongo
        self.collection = "logs"

    def create(self, data: dict):
        return self.mongo.insert_log(self.collection, data)

    def get_all(self) -> List[dict]:
        logs = list(self.mongo.db[self.collection].find())
        
        for log in logs:
            log["_id"] = str(log["_id"])
        
        return logs

    def get_by_id(self, log_id: str) -> Optional[dict]:
        log = self.mongo.db[self.collection].find_one({
            "_id": ObjectId(log_id)
        })

        if log:
            log["_id"] = str(log["_id"])

        return log

    def get_by_event(self, event: str) -> List[dict]:
        logs = list(self.mongo.db[self.collection].find({
            "event": event
        }))

        for log in logs:
            log["_id"] = str(log["_id"])

        return logs

    def delete(self, log_id: str) -> bool:
        result = self.mongo.db[self.collection].delete_one({
            "_id": ObjectId(log_id)
        })

        return result.deleted_count > 0

    def delete_all(self):
        result = self.mongo.db[self.collection].delete_many({})
        return result.deleted_count

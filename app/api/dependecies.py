from dotenv import load_dotenv
import os
from app.db.sql.engine import PostgresEngine
from app.db.mongo.mongo_client import MongoClientManager
from app.db.redis.redis_client import RedisClient

def get_db():
    load_dotenv()
    database_url = os.getenv("database_url")
    db = PostgresEngine(database_url).get_session()
    try:
        yield db
    finally:
        db.close()

def get_mongo():
    load_dotenv()
    uri = os.getenv("mongo_uri")
    database = os.getenv("mongo_db")
    mongo = MongoClientManager(uri=uri, database=database)
    return mongo

def get_redis():
    load_dotenv()
    host = os.getenv("redis_host")
    port = int(os.getenv("redis_port"))
    redis_n_db = int(os.getenv("redis_n_db"))
    redis = RedisClient(
        host=host,
        port=port,
        db=redis_n_db
    )
    return redis

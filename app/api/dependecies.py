from dotenv import load_dotenv
import os
from app.db.sql.engine import PostgresEngine

def get_db():
    load_dotenv()
    database_url = os.getenv("database_url")
    db = PostgresEngine(database_url).get_session()
    try:
        yield db
    finally:
        db.close()

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Postgres
    database_url: str = Field(..., env="DATABASE_URL")

    # Redis
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: int = Field(..., env="REDIS_PORT")
    redis_n_db: int = Field(..., env="REDIS_N_DB")

    # Mongo
    mongo_uri: str = Field(..., env="MONGO_URI")
    mongo_db: str = Field(..., env="MONGO_DB")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"



settings = Settings()
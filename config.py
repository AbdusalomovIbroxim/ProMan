import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")

    if not all([DB_USER, DB_PASSWORD, DB_NAME, DB_HOST]):
        raise ValueError("Некоторые переменные окружения не заданы.")

    DB_CONFIG = "postgresql+asyncpg://postgres:0@localhost/postgres"

    # DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

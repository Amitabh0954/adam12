import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

class Config:
    APP_NAME = os.getenv("APP_NAME", "FlaskApp")
    ENV = os.getenv("ENV", "production")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Database
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # JWT
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_EXPIRY_MINUTES = int(os.getenv("JWT_EXPIRY_MINUTES", 60))

# config/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env if present

class Config:
    APP_NAME = os.getenv("APP_NAME", "FlaskApp")
    ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")

    DATABASE_URL = os.getenv("DATABASE_URL")

    BASE_FILE_PATH = os.getenv("BASE_FILE_PATH", "/tmp")
    LOG_PATH = os.getenv("LOG_PATH", "/tmp")

    JWT_SECRET = os.getenv("JWT_SECRET")
    PAYMENT_GATEWAY_KEY = os.getenv("PAYMENT_GATEWAY_KEY")
    ANALYTICS_KEY = os.getenv("ANALYTICS_KEY")

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TIMEOUT = int(os.environ.get("SESSION_TIMEOUT", 3600))
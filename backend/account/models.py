from typing import Any, Optional
from datetime import datetime, timedelta
import uuid

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

class PasswordResetToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(36), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('reset_tokens', lazy=True))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow() + timedelta(hours=24))

    def __init__(self, user: User) -> None:
        self.user = user
        self.token = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.expires_at = self.created_at + timedelta(hours=24)

    @staticmethod
    def validate_token(token: str) -> Optional['PasswordResetToken']:
        token_object = PasswordResetToken.query.filter_by(token=token).first()
        if token_object and datetime.utcnow() < token_object.expires_at:
            return token_object
        return None
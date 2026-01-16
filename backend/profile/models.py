from typing import Any
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    preferences = db.Column(db.JSON, nullable=True)

    user = db.relationship('User', backref=db.backref('profile', uselist=False))

    def __init__(self, user_id: int, first_name: str = '', last_name: str = '', preferences: Any = None) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.preferences = preferences if preferences is not None else {}
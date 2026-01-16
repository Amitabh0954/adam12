from typing import List
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    children = db.relationship('Category', backref=db.backref('parent', remote_side=[id]), lazy='dynamic')

    def __init__(self, name: str, parent_id: int = None) -> None:
        self.name = name
        self.parent_id = parent_id

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('products', lazy=True))
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name: str, price: float, description: str, category_id: int) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.category_id = category_id
        self.is_deleted = False
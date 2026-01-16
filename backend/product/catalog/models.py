from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name: str, price: float, description: str, category: str = '') -> None:
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.is_deleted = False
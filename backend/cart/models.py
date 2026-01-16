from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    items = relationship('CartItem', back_populates='cart', cascade='all, delete-orphan')

    def __init__(self, user_id: int = None) -> None:
        self.user_id = user_id

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    cart = relationship('Cart', back_populates='items')
    product = relationship('Product')

    def __init__(self, cart_id: int, product_id: int, quantity: int = 1) -> None:
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity
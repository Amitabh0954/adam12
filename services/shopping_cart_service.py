# Shopping Cart FunctionalityImplement a shopping cart system that allows users to add, remove, and modify products in their cart. This includes saving the cart state for logged-in users and guest checkouts.EPIC-3
from sqlalchemy.orm import Session
from models.product import Product
from models.cart import Cart

class ShoppingCartService:
    def __init__(self, session: Session):
        self.session = session

    def add_product(self, user_id, product_id, quantity):
        cart = self.session.query(Cart).filter_by(user_id=user_id).first()
        product = self.session.query(Product).filter_by(id=product_id).first()
        if not cart:
            cart = Cart(user_id=user_id)
            self.session.add(cart)
        cart.add_product(product, quantity)
        self.session.commit()
        return cart

    def remove_product(self, user_id, product_id):
        cart = self.session.query(Cart).filter_by(user_id=user_id).first()
        if cart:
            cart.remove_product(product_id)
            self.session.commit()
        return cart

    def modify_product_quantity(self, user_id, product_id, quantity):
        cart = self.session.query(Cart).filter_by(user_id=user_id).first()
        if cart:
            cart.modify_product_quantity(product_id, quantity)
            self.session.commit()
        return cart

    def get_cart(self, user_id):
        cart = self.session.query(Cart).filter_by(user_id=user_id).first()
        return cart
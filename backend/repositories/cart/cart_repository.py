from typing import Optional
from backend.models.cart.shopping_cart import ShoppingCart

class CartRepository:
    def __init__(self):
        self.carts = {}

    def load_cart(self, user_id: int) -> ShoppingCart:
        return self.carts.get(user_id, ShoppingCart(user_id=user_id))

    def save_cart(self, cart: ShoppingCart):
        self.carts[cart.user_id] = cart
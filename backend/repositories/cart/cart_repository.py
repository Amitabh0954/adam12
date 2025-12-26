from models.cart import Cart, CartItem
from typing import Optional

class CartRepository:
    def __init__(self):
        self.carts = []

    def find_by_user_id(self, user_id: int) -> Optional[Cart]:
        return next((cart for cart in self.carts if cart.user_id == user_id), None)

    def save(self, cart: Cart) -> None:
        existing_cart = self.find_by_user_id(cart.user_id)
        if existing_cart:
            self.carts = [cart if c.user_id == cart.user_id else c for c in self.carts]
        else:
            self.carts.append(cart)
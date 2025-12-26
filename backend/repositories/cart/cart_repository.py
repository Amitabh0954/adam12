from models.cart import ShoppingCart
from typing import Optional

class CartRepository:
    def __init__(self):
        self.carts = {}

    def find_by_user_id(self, user_id: int) -> Optional[ShoppingCart]:
        return self.carts.get(user_id)

    def save(self, cart: ShoppingCart) -> None:
        self.carts[cart.user_id] = cart

    def clear_cart(self, user_id: int) -> None:
        if user_id in self.carts:
            del self.carts[user_id]
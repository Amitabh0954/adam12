from models.cart import Cart
from typing import List

class CartRepository:
    def __init__(self):
        self.cart_items = []

    def find_by_user_id(self, user_id: int) -> List[Cart]:
        return [item for item in self.cart_items if item.user_id == user_id]

    def save(self, cart_item: Cart) -> None:
        self.cart_items.append(cart_item)

    def remove_item(self, user_id: int, product_id: int) -> None:
        self.cart_items = [item for item in self.cart_items if not (item.user_id == user_id and item.product_id == product_id)]
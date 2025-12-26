from models.cart import Cart
from typing import List, Optional

class CartRepository:
    def __init__(self):
        self.cart_items = []

    def find_by_user_id(self, user_id: int) -> List[Cart]:
        return [item for item in self.cart_items if item.user_id == user_id]

    def find_by_user_and_product(self, user_id: int, product_id: int) -> Optional[Cart]:
        return next((item for item in self.cart_items if item.user_id == user_id and item.product_id == product_id), None)

    def save(self, cart_item: Cart) -> None:
        existing_item = self.find_by_user_and_product(cart_item.user_id, cart_item.product_id)
        if existing_item:
            existing_item.quantity = cart_item.quantity
        else:
            self.cart_items.append(cart_item)

    def remove_item(self, user_id: int, product_id: int) -> None:
        self.cart_items = [item for item in self.cart_items if not (item.user_id == user_id and item.product_id == product_id)]
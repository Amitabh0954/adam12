from models.cart_item import CartItem
from typing import Optional, List

class CartRepository:
    def __init__(self):
        self.cart_items = []
        self.next_id = 1

    def find_all_by_user(self, user_id: int) -> List[CartItem]:
        return [item for item in self.cart_items if item.user_id == user_id]

    def find_by_user_and_product(self, user_id: int, product_id: int) -> Optional[CartItem]:
        return next((item for item in self.cart_items if item.user_id == user_id and item.product_id == product_id), None)

    def save(self, cart_item: CartItem) -> None:
        if cart_item.id is None:
            cart_item.id = self.next_id
            self.next_id += 1
            self.cart_items.append(cart_item)
        else:
            self.cart_items = [cart_item if cart_item.id == item.id else item for item in self.cart_items]

    def delete(self, cart_item_id: int) -> None:
        self.cart_items = [item for item in self.cart_items if item.id != cart_item_id]
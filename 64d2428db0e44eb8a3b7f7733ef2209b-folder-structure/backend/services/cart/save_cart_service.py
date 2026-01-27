# Epic Title: Shopping Cart Functionality

from backend.repositories.cart.cart_repository import CartRepository
from typing import Dict

class SaveCartService:
    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository

    def save_cart_for_user(self, user_id: int, cart_id: int) -> bool:
        cart = self.cart_repository.get_cart_by_id(cart_id)
        if not cart or cart.user_id != user_id:
            raise ValueError("Cart does not belong to the user")
        self.cart_repository.save_cart(cart)
        return True

    def retrieve_cart_for_user(self, user_id: int) -> Dict:
        cart = self.cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            raise ValueError("No saved cart found for the user")
        items = self.cart_repository.get_items_by_cart_id(cart.cart_id)
        return {
            "cart_id": cart.cart_id,
            "user_id": cart.user_id,
            "is_guest": cart.is_guest,
            "items": [{"cart_item_id": item.cart_item_id, "product_id": item.product_id, "quantity": item.quantity} for item in items]
        }
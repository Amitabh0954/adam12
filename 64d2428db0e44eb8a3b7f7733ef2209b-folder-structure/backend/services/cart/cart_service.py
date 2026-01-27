# Epic Title: Shopping Cart Functionality

from backend.models.cart.cart import Cart
from backend.models.cart.cart_item import CartItem
from backend.repositories.cart.cart_repository import CartRepository
from backend.repositories.product.product_repository import ProductRepository
from typing import List, Dict

class CartService:
    def __init__(self, cart_repository: CartRepository, product_repository: ProductRepository):
        self.cart_repository = cart_repository
        self.product_repository = product_repository

    def create_cart_for_user(self, user_id: int) -> Cart:
        cart = Cart(cart_id=0, user_id=user_id, is_guest=False)  # Example ID management
        self.cart_repository.create_cart(cart)
        return cart

    def create_guest_cart(self) -> Cart:
        cart = Cart(cart_id=0, is_guest=True)  # Example ID management
        self.cart_repository.create_cart(cart)
        return cart

    def add_product_to_cart(self, cart_id: int, product_id: int, quantity: int) -> CartItem:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product does not exist")
        cart_item = CartItem(cart_item_id=0, cart_id=cart_id, product_id=product_id, quantity=quantity)  # Example ID management
        self.cart_repository.add_item_to_cart(cart_item)
        return cart_item

    def get_cart_items(self, cart_id: int) -> List[Dict]:
        items = self.cart_repository.get_items_by_cart_id(cart_id)
        return [
            {
                "cart_item_id": item.cart_item_id,
                "product_id": item.product_id,
                "quantity": item.quantity
            }
            for item in items
        ]
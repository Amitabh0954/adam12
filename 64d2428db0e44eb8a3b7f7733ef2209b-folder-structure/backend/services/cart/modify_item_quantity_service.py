# Epic Title: Shopping Cart Functionality

from backend.repositories.cart.cart_repository import CartRepository
from backend.repositories.product.product_repository import ProductRepository

class ModifyItemQuantityService:
    def __init__(self, cart_repository: CartRepository, product_repository: ProductRepository):
        self.cart_repository = cart_repository
        self.product_repository = product_repository

    def modify_item_quantity(self, cart_id: int, cart_item_id: int, quantity: int) -> bool:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        item = self.cart_repository.get_cart_item_by_id(cart_item_id)
        if not item or item.cart_id != cart_id:
            raise ValueError("Item does not exist in the cart")
        item.quantity = quantity
        self.cart_repository.update_item_quantity(item)
        return True
# Epic Title: Shopping Cart Functionality

from backend.models.cart.cart import Cart
from backend.models.cart.cart_item import CartItem
from typing import Optional, List

class CartRepository:
    def __init__(self):
        # Initialize database connection here
        pass

    def create_cart(self, cart: Cart) -> None:
        # logic to create a new cart in the database
        pass

    def get_cart_by_id(self, cart_id: int) -> Optional[Cart]:
        # logic to retrieve a cart by id
        pass

    def get_cart_by_user_id(self, user_id: int) -> Optional[Cart]:
        # logic to retrieve a cart by user id
        pass

    def add_item_to_cart(self, cart_item: CartItem) -> None:
        # logic to add an item to a cart in the database
        pass

    def get_items_by_cart_id(self, cart_id: int) -> List[CartItem]:
        # logic to retrieve all items in a cart by cart id
        pass

    def get_cart_item_by_id(self, cart_item_id: int) -> Optional[CartItem]:
        # logic to retrieve a cart item by id
        pass

    def remove_item_from_cart(self, cart_item_id: int) -> None:
        # logic to remove a cart item from the database
        pass

    def update_item_quantity(self, cart_item: CartItem) -> None:
        # logic to update the quantity of an item in the cart in the database
        pass

    def save_cart(self, cart: Cart) -> None:
        # logic to save the current state of the cart
        pass
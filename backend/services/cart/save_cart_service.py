from backend.models.cart.shopping_cart import ShoppingCart
from backend.repositories.cart.cart_repository import CartRepository

cart_repository = CartRepository()

def save_cart_for_user(user_id: int):
    cart = cart_repository.load_cart(user_id)
    cart_repository.save_cart(cart)

def get_saved_cart_for_user(user_id: int) -> ShoppingCart:
    return cart_repository.load_cart(user_id)
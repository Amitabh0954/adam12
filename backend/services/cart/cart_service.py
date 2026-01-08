from typing import Optional
from backend.models.cart.cart_item import CartItem
from backend.models.cart.shopping_cart import ShoppingCart
from backend.repositories.cart.cart_repository import CartRepository

cart_repository = CartRepository()

def get_cart(user_id: Optional[int]) -> ShoppingCart:
    if user_id:
        return cart_repository.load_cart(user_id)
    else:
        return ShoppingCart()

def add_product_to_cart(user_id: Optional[int], cart_item: CartItem) -> ShoppingCart:
    cart = get_cart(user_id)
    for item in cart.items:
        if item.product.id == cart_item.product.id:
            item.quantity += cart_item.quantity
            break
    else:
        cart.items.append(cart_item)
    return cart

def save_cart(cart: ShoppingCart):
    if cart.user_id:
        cart_repository.save_cart(cart)
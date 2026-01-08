from typing import Optional
from backend.models.cart.shopping_cart import ShoppingCart
from backend.services.cart.cart_service import save_cart, get_cart

def remove_product_from_cart(user_id: Optional[int], product_id: int) -> ShoppingCart:
    cart = get_cart(user_id)
    updated_items = [item for item in cart.items if item.product.id != product_id]

    if len(updated_items) == len(cart.items):
        raise ValueError("Item not found in cart")

    cart.items = updated_items
    save_cart(cart)
    return cart
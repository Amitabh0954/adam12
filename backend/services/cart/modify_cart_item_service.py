from typing import Optional
from backend.models.cart.shopping_cart import ShoppingCart
from backend.services.cart.cart_service import save_cart, get_cart

def modify_product_quantity_in_cart(user_id: Optional[int], product_id: int, quantity: int) -> ShoppingCart:
    cart = get_cart(user_id)
    for item in cart.items:
        if item.product.id == product_id:
            item.quantity = quantity
            break
    else:
        raise ValueError("Item not found in cart")
    
    save_cart(cart)
    return cart
from typing import List, Optional
from pydantic import BaseModel
from backend.models.cart.cart_item import CartItem

class ShoppingCart(BaseModel):
    user_id: Optional[int] = None
    items: List[CartItem] = []
# Epic Title: Shopping Cart Functionality

class CartItem:
    cart_item_id: int
    cart_id: int
    product_id: int
    quantity: int

    def __init__(self, cart_item_id: int, cart_id: int, product_id: int, quantity: int):
        self.cart_item_id = cart_item_id
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity
from datetime import datetime

class CartItem:
    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity
        self.added_at = datetime.utcnow()

class Cart:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.items = []

    def add_item(self, product_id: int, quantity: int):
        self.items.append(CartItem(product_id, quantity))
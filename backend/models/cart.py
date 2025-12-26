from datetime import datetime
from typing import List

class CartItem:
    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity
        self.added_at = datetime.utcnow()

class ShoppingCart:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.items: List[CartItem] = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def add_item(self, product_id: int, quantity: int):
        item = next((i for i in self.items if i.product_id == product_id), None)
        if item:
            item.quantity += quantity
        else:
            self.items.append(CartItem(product_id, quantity))
        self.updated_at = datetime.utcnow()

    def remove_item(self, product_id: int):
        self.items = [i for i in self.items if i.product_id != product_id]
        self.updated_at = datetime.utcnow()

    def clear(self):
        self.items = []
        self.updated_at = datetime.utcnow()

    def update_quantity(self, product_id: int, quantity: int):
        item = next((i for i in self.items if i.product_id == product_id), None)
        if item:
            item.quantity = quantity
        self.updated_at = datetime.utcnow()

    def calculate_total(self):
        total = sum(item.quantity * item.product_price for item in self.items)
        return total
from datetime import datetime

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

class Cart:
    def __init__(self, user_id: int = None):
        self.user_id = user_id
        self.items = []
        self.total_price = 0.0
        self.created_at = datetime.utcnow()
        self.updated_at = None
    
    def add_item(self, product: Product, quantity: int):
        self.items.append(CartItem(product, quantity))
        self.total_price += product.price * quantity
        self.updated_at = datetime.utcnow()
    
    def remove_item(self, product: Product):
        for item in self.items:
            if item.product == product:
                self.total_price -= item.product.price * item.quantity
                self.items.remove(item)
                break
        self.updated_at = datetime.utcnow()
    
    def modify_quantity(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        for item in self.items:
            if item.product == product:
                self.total_price -= item.product.price * item.quantity
                item.quantity = quantity
                self.total_price += item.product.price * item.quantity
                break
        self.updated_at = datetime.utcnow()
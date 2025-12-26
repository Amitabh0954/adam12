from datetime import datetime

class Cart:
    def __init__(self, user_id: int = None):
        self.user_id = user_id
        self.items = []
        self.total_price = 0.0
        self.created_at = datetime.utcnow()
        self.updated_at = None
    
    def add_item(self, product: Product):
        self.items.append(product)
        self.total_price += product.price
        self.updated_at = datetime.utcnow()
    
    def remove_item(self, product: Product):
        self.items.remove(product)
        self.total_price -= product.price
        self.updated_at = datetime.utcnow()
from datetime import datetime

class Cart:
    def __init__(self, user_id: int = None):
        self.user_id = user_id
        self.items = []
        self.created_at = datetime.utcnow()
        self.updated_at = None
    
    def add_item(self, product_id: int):
        self.items.append(product_id)
        self.updated_at = datetime.utcnow()
    
    def remove_item(self, product_id: int):
        self.items.remove(product_id)
        self.updated_at = datetime.utcnow()
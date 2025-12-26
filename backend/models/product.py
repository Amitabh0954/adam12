from datetime import datetime

class Product:
    def __init__(self, name: str, price: float, description: str, category_id: int):
        self.name = name
        self.price = price
        self.description = description
        self.category_id = category_id
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.is_deleted = False
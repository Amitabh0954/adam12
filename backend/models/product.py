from datetime import datetime

class Product:
    def __init__(self, name: str, price: float, description: str):
        self.id = None  # This should be set by the repository when saved
        self.name = name
        self.price = price
        self.description = description
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, name: str = None, price: float = None, description: str = None):
        if name:
            self.name = name
        if price:
            self.price = price
        if description:
            self.description = description
        self.updated_at = datetime.utcnow()
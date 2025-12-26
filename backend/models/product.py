class Product:
    def __init__(self, name: str, price: float, description: str, category_id: int):
        self.name = name
        self.price = price
        self.description = description
        self.category_id = category_id
        self.updated_at = None
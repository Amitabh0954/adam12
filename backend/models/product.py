class Product:
    def __init__(self, id: int, name: str, price: float, description: str, category_id: int):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category_id = category_id
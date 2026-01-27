# Epic Title: Product Catalog Management

class Product:
    product_id: int
    name: str
    description: str
    price: float

    def __init__(self, product_id: int, name: str, description: str, price: float):
        if price <= 0:
            raise ValueError("Price must be a positive number")
        if not name:
            raise ValueError("Product name cannot be empty")
        if not description:
            raise ValueError("Product description cannot be empty")
        
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
    
    def update_product(self, name: str, description: str, price: float):
        if price <= 0:
            raise ValueError("Price must be a positive number")
        if not name:
            raise ValueError("Product name cannot be empty")
        if not description:
            raise ValueError("Product description cannot be empty")
        
        self.name = name
        self.description = description
        self.price = price
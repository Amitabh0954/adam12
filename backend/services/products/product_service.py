from repositories.products.product_repository import ProductRepository
from models.product import Product
from typing import Optional

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float, category_id: int):
        if not name or not description or price is None or price <= 0:
            return {"message": "Invalid product details", "status": 400}

        if self.product_repository.find_by_name(name):
            return {"message": "Product name already exists", "status": 400}

        product = Product(id=None, name=name, description=description, price=price, category_id=category_id)
        self.product_repository.save(product)
        return {"message": "Product added successfully", "status": 201, "product": {"id": product.id, "name": product.name, "description": product.description, "price": product.price}}
import logging
from typing import Optional
from backend.models.products.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []

    def get_by_name(self, name: str) -> Optional[Product]:
        for product in self.products:
            if product.name == name:
                return product
        return None

    def save(self, product: Product):
        if not product.id:
            product.id = len(self.products) + 1
        self.products.append(product)
        logging.info(f"Product with name {product.name} saved successfully.")
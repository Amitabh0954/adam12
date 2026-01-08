import logging
from typing import Optional, List
from backend.models.products.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []

    def get_by_id(self, product_id: int) -> Optional[Product]:
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def get_by_name(self, name: str) -> Optional[Product]:
        for product in self.products:
            if product.name == name:
                return product
        return None

    def search(self, query: str) -> List[Product]:
        query_lower = query.lower()
        return [product for product in self.products
                if query_lower in product.name.lower()
                or query_lower in product.description.lower()]

    def save(self, product: Product):
        if not product.id:
            product.id = len(self.products) + 1
        self.products.append(product)
        logging.info(f"Product with name {product.name} saved successfully.")

    def delete(self, product_id: int):
        self.products = [product for product in self.products if product.id != product_id]
        logging.info(f"Product with id {product_id} deleted successfully.")
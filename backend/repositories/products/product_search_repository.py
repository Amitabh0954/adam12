from models.product import Product
from typing import List, Optional

class ProductSearchRepository:
    def __init__(self):
        self.products = [
            # Example products
            Product(name="Product1", price=100.0, description="Description of Product1"),
            Product(name="Product2", price=150.0, description="Description of Product2"),
            Product(name="Product3", price=200.0, description="Description of Product3")
        ]

    def search_products(self, query: str, page: int, per_page: int) -> List[Product]:
        filtered_products = [
            product for product in self.products if query.lower() in product.name.lower() or query.lower() in product.description.lower()
        ]
        start = (page - 1) * per_page
        end = start + per_page
        return filtered_products[start:end]

    def total_products(self, query: str) -> int:
        return len([
            product for product in self.products if query.lower() in product.name.lower() or query.lower() in product.description.lower()
        ])
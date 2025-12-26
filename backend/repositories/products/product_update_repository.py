from models.product import Product
from typing import List, Optional

class ProductUpdateRepository:
    def __init__(self):
        self.products = []

    def find_by_id(self, product_id: int) -> Optional[Product]:
        return next((product for product in self.products if product.id == product_id), None)

    def save(self, product: Product) -> None:
        self.products = [product if product.id == p.id else p for p in self.products]
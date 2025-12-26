from models.product import Product
from typing import List, Optional

class ProductDeleteRepository:
    def __init__(self):
        self.products = []

    def find_by_id(self, product_id: int) -> Optional[Product]:
        return next((product for product in self.products if product.id == product_id), None)

    def delete(self, product_id: int) -> None:
        self.products = [product for product in self.products if product.id != product_id]
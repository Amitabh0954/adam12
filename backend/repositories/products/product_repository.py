from models.product import Product
from typing import Optional, List

class ProductRepository:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def find_all(self) -> List[Product]:
        return self.products

    def find_by_id(self, product_id: int) -> Optional[Product]:
        return next((product for product in self.products if product.id == product_id), None)

    def find_by_name(self, name: str) -> Optional[Product]:
        return next((product for product in self.products if product.name == name), None)

    def save(self, product: Product) -> None:
        if product.id is None:
            product.id = self.next_id
            self.next_id += 1
            self.products.append(product)
        else:
            self.products = [product if product.id == p.id else p for p in self.products]
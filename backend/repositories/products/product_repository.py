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

    def search(self, query: str, page: int, per_page: int) -> List[Product]:
        results = [product for product in self.products if query.lower() in product.name.lower() or query.lower() in product.description.lower()]
        start = (page - 1) * per_page
        end = start + per_page
        return results[start:end]

    def save(self, product: Product) -> None:
        if product.id is None:
            product.id = self.next_id
            self.next_id += 1
            self.products.append(product)
        else:
            self.products = [product if product.id == p.id else p for p in self.products]

    def delete(self, product_id: int) -> None:
        self.products = [product for product in self.products if product.id != product_id]
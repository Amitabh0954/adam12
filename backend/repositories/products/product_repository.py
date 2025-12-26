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

    def delete(self, product_id: int) -> None:
        self.products = [product for product in self.products if product.id != product_id]
    
    def search(self, query: str) -> List[Product]:
        query = query.lower()
        return [product for product in self.products if query in product.name.lower() or query in product.description.lower() or query in str(product.category_id)]
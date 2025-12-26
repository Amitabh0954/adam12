from models.product_category import ProductCategory
from typing import List

class ProductCategoryRepository:
    def __init__(self):
        self.product_categories = []

    def save(self, product_category: ProductCategory) -> None:
        self.product_categories.append(product_category)

    def find_by_product_id(self, product_id: int) -> List[ProductCategory]:
        return [pc for pc in self.product_categories if pc.product_id == product_id]

    def find_by_category_id(self, category_id: int) -> List[ProductCategory]:
        return [pc for pc in self.product_categories if pc.category_id == category_id]
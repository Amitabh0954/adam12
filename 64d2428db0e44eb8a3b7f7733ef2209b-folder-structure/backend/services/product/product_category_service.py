# Epic Title: Product Catalog Management

from backend.models.product.product_category import ProductCategory
from backend.repositories.product.product_category_repository import ProductCategoryRepository
from typing import List

class ProductCategoryService:
    def __init__(self, product_category_repository: ProductCategoryRepository):
        self.product_category_repository = product_category_repository
    
    def assign_category_to_product(self, product_id: int, category_id: int) -> ProductCategory:
        product_category = ProductCategory(product_id, category_id)
        self.product_category_repository.add_product_category(product_category)
        return product_category

    def get_categories_for_product(self, product_id: int) -> List[int]:
        return self.product_category_repository.get_categories_by_product_id(product_id)
    
    def get_products_for_category(self, category_id: int) -> List[int]:
        return self.product_category_repository.get_products_by_category_id(category_id)
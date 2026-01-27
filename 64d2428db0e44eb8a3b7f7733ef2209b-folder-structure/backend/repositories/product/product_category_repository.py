# Epic Title: Product Catalog Management

from backend.models.product.product_category import ProductCategory
from typing import List

class ProductCategoryRepository:
    def __init__(self):
        # Initialize database connection here
        pass

    def add_product_category(self, product_category: ProductCategory) -> None:
        # logic to add product category to the database
        pass

    def get_categories_by_product_id(self, product_id: int) -> List[int]:
        # logic to retrieve categories by product id
        pass
    
    def get_products_by_category_id(self, category_id: int) -> List[int]:
        # logic to retrieve products by category id
        pass
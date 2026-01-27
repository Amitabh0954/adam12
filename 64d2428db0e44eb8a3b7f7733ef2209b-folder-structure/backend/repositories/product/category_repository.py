# Epic Title: Product Catalog Management

from backend.models.product.category import Category
from typing import Optional, List

class CategoryRepository:
    def __init__(self):
        # Initialize database connection here
        pass

    def add_category(self, category: Category) -> None:
        # logic to add category to the database
        pass

    def get_category_by_id(self, category_id: int) -> Optional<Category]:
        # logic to retrieve a category by id
        pass

    def get_all_categories(self) -> List[Category]:
        # logic to retrieve all categories
        pass

    def update_category(self, category: Category) -> None:
        # logic to update the category in the database
        pass
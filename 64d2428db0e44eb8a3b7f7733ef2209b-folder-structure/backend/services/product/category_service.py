# Epic Title: Product Catalog Management

from backend.models.product.category import Category
from backend.repositories.product.category_repository import CategoryRepository
from typing import List

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def create_category(self, name: str, parent_id: int = None) -> Category:
        new_category = Category(category_id=0, name=name, parent_id=parent_id)  # Example ID management
        self.category_repository.add_category(new_category)
        return new_category

    def update_category(self, category_id: int, name: str):
        category = self.category_repository.get_category_by_id(category_id)
        if not category:
            raise ValueError("Category does not exist")
        category.update_category(name)
        self.category_repository.update_category(category)
        return category

    def get_all_categories(self) -> List[Category]:
        return self.category_repository.get_all_categories()
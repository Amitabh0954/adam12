from typing import List, Optional
from backend.models.products.category import Category

class CategoryRepository:
    def __init__(self):
        self.categories = []

    def get_by_name(self, name: str) -> Optional[Category]:
        for category in self.categories:
            if category.name == name:
                return category
        return None

    def get_all(self) -> List[Category]:
        return self.categories

    def save(self, category: Category):
        if not category.id:
            category.id = len(self.categories) + 1
        self.categories.append(category)

    def delete(self, category_id: int):
        self.categories = [category for category in self.categories if category.id != category_id]
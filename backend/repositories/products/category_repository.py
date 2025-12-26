from models.category import Category
from typing import List, Optional

class CategoryRepository:
    def __init__(self):
        self.categories = []
        self.next_id = 1

    def find_by_id(self, category_id: int) -> Optional[Category]:
        return next((category for category in self.categories if category.id == category_id), None)

    def save(self, category: Category) -> None:
        if category.id is None:
            category.id = self.next_id
            self.next_id += 1
            self.categories.append(category)
        else:
            self.categories = [category if category.id == c.id else c for c in self.categories]

    def get_all(self) -> List[Category]:
        return self.categories
from typing import List, Dict
from backend.models.products.category import Category
from backend.repositories.products.category_repository import CategoryRepository

category_repository = CategoryRepository()

def add_category(category: Category):
    if category_repository.get_by_name(category.name):
        raise ValueError("Category name must be unique")
    category_repository.save(category)

def get_all_categories() -> List[Dict]:
    categories = category_repository.get_all()
    return [category.dict() for category in categories]
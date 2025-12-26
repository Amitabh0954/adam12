from repositories.products.category_repository import CategoryRepository
from models.category import Category
from typing import Optional

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: Optional[int] = None):
        if not name:
            return {"message": "Category name is required", "status": 400}

        if self.category_repository.find_by_name(name):
            return {"message": "Category name already exists", "status": 400}

        category = Category(id=None, name=name, parent_id=parent_id)
        self.category_repository.save(category)
        return {"message": "Category added successfully", "status": 201, "category": {"id": category.id, "name": category.name, "parent_id": category.parent_id}}
    
    def get_categories(self):
        categories = self.category_repository.find_all()
        return {"message": "Categories retrieved successfully", "status": 200, "categories": [{"id": category.id, "name": category.name, "parent_id": category.parent_id} for category in categories]}
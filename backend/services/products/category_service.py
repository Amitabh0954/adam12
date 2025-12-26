from repositories.products.category_repository import CategoryRepository
from models.category import Category
from typing import Optional, List

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, description: str, parent_id: Optional[int]):
        if not name:
            return {"message": "Category name is required", "status": 400}

        if self.category_repository.find_by_name(name):
            return {"message": "Category name already exists", "status": 400}

        category = Category(id=None, name=name, description=description, parent_id=parent_id)
        self.category_repository.save(category)
        return {"message": "Category added successfully", "status": 201, "category": {"id": category.id, "name": category.name, "description": category.description, "parent_id": category.parent_id}}

    def update_category(self, category_id: int, name: Optional[str], description: Optional[str]):
        category = self.category_repository.find_by_id(category_id)
        if not category:
            return {"message": "Category not found", "status": 404}

        if name is not None:
            if self.category_repository.find_by_name(name) and self.category_repository.find_by_name(name).id != category_id:
                return {"message": "Category name already exists", "status": 400}
            category.name = name
        
        if description is not None:
            category.description = description

        self.category_repository.save(category)
        return {"message": "Category updated successfully", "status": 200, "category": {"id": category.id, "name": category.name, "description": category.description, "parent_id": category.parent_id}}

    def delete_category(self, category_id: int):
        category = self.category_repository.find_by_id(category_id)
        if not category:
            return {"message": "Category not found", "status": 404}

        self.category_repository.delete(category_id)
        return {"message": "Category deleted successfully", "status": 200}

    def get_categories(self):
        categories = self.category_repository.find_all()
        return {"categories": [{"id": category.id, "name": category.name, "description": category.description, "parent_id": category.parent_id} for category in categories], "status": 200}
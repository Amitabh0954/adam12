from repositories.categories.category_repository import CategoryRepository
from models.category import Category

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()
    
    def add_category(self, data: dict):
        name = data.get('name')
        parent_id = data.get('parent_id', None)
        
        if not name:
            return {"message": "Category name is required", "status": 400}
        
        existing_category = self.category_repository.find_by_name(name)
        if existing_category:
            return {"message": "Category name already exists", "status": 400}
        
        category = Category(name=name, parent_id=parent_id)
        self.category_repository.save(category)
        
        return {"message": "Category added successfully", "status": 201}
    
    def get_categories(self):
        categories = self.category_repository.categories
        return {"categories": categories, "status": 200}
    
    def update_category(self, category_id: int, data: dict):
        category = self.category_repository.find_by_id(category_id)
        if not category:
            return {"message": "Category not found", "status": 404}
        
        name = data.get('name')
        parent_id = data.get('parent_id')
        
        if name:
            existing_category = self.category_repository.find_by_name(name)
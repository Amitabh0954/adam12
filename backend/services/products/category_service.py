from repositories.products.category_repository import CategoryRepository
from models.category import Category

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, data: dict):
        name = data.get('name')
        parent_id = data.get('parent_id', None)

        if not name:
            return {"message": "Category name is required", "status": 400}

        category = Category(name=name, parent_id=parent_id)
        self.category_repository.save(category)

        return {"message": "Category added successfully", "status": 201, "category": category.__dict__}

    def get_category(self, category_id: int):
        category = self.category_repository.find_by_id(category_id)
        if not category:
            return {"message": "Category not found", "status": 404}

        return {"message": "Category retrieved successfully", "status": 200, "category": category.__dict__}

    def get_all_categories(self):
        categories = self.category_repository.get_all()
        return {"message": "All categories retrieved successfully", "status": 200, "categories": [category.__dict__ for category in categories]}
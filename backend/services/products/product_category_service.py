from repositories.products.product_category_repository import ProductCategoryRepository, CategoryRepository
from models.product_category import ProductCategory

class ProductCategoryService:
    def __init__(self):
        self.product_category_repository = ProductCategoryRepository()
        self.category_repository = CategoryRepository()

    def assign_category(self, product_id: int, category_id: int):
        category = self.category_repository.find_by_id(category_id)
        if not category:
            return {"message": "Category not found", "status": 404}

        product_category = ProductCategory(product_id=product_id, category_id=category_id)
        self.product_category_repository.save(product_category)

        return {"message": "Category assigned to product successfully", "status": 201}
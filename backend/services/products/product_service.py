from repositories.products.product_repository import ProductRepository
from repositories.products.category_repository import CategoryRepository
from models.product import Product
from models.category import Category
from datetime import datetime

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.category_repository = CategoryRepository()
    
    def add_product(self, data: dict):
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        category_id = data.get('category_id')
        
        if not name or not price or price <= 0 or not description or not category_id:
            return {"message": "Invalid product data", "status": 400}
        
        existing_product = self.product_repository.find_by_name(name)
        if existing_product:
            return {"message": "Product name already exists", "status": 400}
        
        product = Product(name=name, price=price, description=description, category_id=category_id)
        self.product_repository.save(product)
        
        return {"message": "Product added to inventory", "status": 201}
    
    def update_product(self, product_id: int, data: dict):
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}
        
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        
        if name:
            existing_product = self.product_repository.find_by_name(name)
            if existing_product:
                return {"message": "Product name already exists", "status": 400}
            product.name = name
            
        if price is not None:
            if not isinstance(price, (int, float)) or price <= 0:
                return {"message": "Invalid price", "status": 400}
            product.price = price
            
        if description:
            product.description = description
        
        product.updated_at = datetime.utcnow()
        self.product_repository.update(product)
        
        return {"message": "Product details updated successfully", "status": 200}
    
    def delete_product(self, product_id: int):
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}
        
        self.product_repository.delete(product)
        
        return {"message": "Product removed from inventory", "status": 200}
    
    def search_products(self, query: str, page: int, per_page: int):
        result = self.product_repository.search(query, page, per_page)
        
        return {"products": result['products'], "total_products": result['total_products'], "page": result['page'], "per_page": result['per_page'], "query": result['query'], "status": 200}

    def add_category(self, data: dict):
        name = data.get('name')
        parent_id = data.get('parent_id')
        
        if not name:
            return {"message": "Category name is required", "status": 400}
        
        existing_category = self.category_repository.find_by_name(name)
        if existing_category:
            return {"message": "Category name already exists", "status": 400}
        
        category = Category(name=name, parent_id=parent_id)
        self.category_repository.save(category)
        
        return {"message": "Category added successfully", "status": 201}

    def update_category(self, category_id: int, data: dict):
        category = self.category_repository.find_by_id(category_id)
        if not category:
            return {"message": "Category not found", "status": 404}
        
        name = data.get('name')
        parent_id = data.get('parent_id')
        
        if name:
            existing_category = self.category_repository.find_by_name(name)
            if existing_category:
                return {"message": "Category name already exists", "status": 400}
            category.name = name
        
        category.parent_id = parent_id
        category.updated_at = datetime.utcnow()
        self.category_repository.update(category)
        
        return {"message": "Category updated successfully", "status": 200}

    def delete_category(self, category_id: int):
        category = self.category_repository.find_by_id(category_id)
        if not category:
            return {"message": "Category not found", "status": 404}
        
        child_categories = self.category_repository.find_children(category_id)
        if child_categories:
            return {"message": "Cannot delete category with subcategories", "status": 400}
        
        self.category_repository.delete(category)
        
        return {"message": "Category deleted successfully", "status": 200}
from repositories.products.product_repository import ProductRepository
from models.product import Product
from datetime import datetime

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()
    
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
            
        if price:
            if price <= 0:
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
        
        return {"message": "Product deleted successfully", "status": 200}
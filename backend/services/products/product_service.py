from repositories.products.product_repository import ProductRepository
from models.product import Product
from typing import Optional, List

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float, category_id: int):
        if not name or not description or price is None or price <= 0:
            return {"message": "Invalid product details", "status": 400}

        if self.product_repository.find_by_name(name):
            return {"message": "Product name already exists", "status": 400}

        product = Product(id=None, name=name, description=description, price=price, category_id=category_id)
        self.product_repository.save(product)
        return {"message": "Product added successfully", "status": 201, "product": {"id": product.id, "name": product.name, "description": product.description, "price": product.price}}

    def update_product(self, product_id: int, name: Optional[str], description: Optional[str], price: Optional[float]):
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}

        if name is not None:
            if self.product_repository.find_by_name(name) and self.product_repository.find_by_name(name).id != product_id:
                return {"message": "Product name already exists", "status": 400}
            product.name = name
        
        if description is not None and description.strip() != "":
            product.description = description
        
        if price is not None:
            if price <= 0:
                return {"message": "Price must be a positive number", "status": 400}
            product.price = price

        self.product_repository.save(product)
        return {"message": "Product updated successfully", "status": 200, "product": {"id": product.id, "name": product.name, "description": product.description, "price": product.price}}

    def delete_product(self, product_id: int):
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}

        self.product_repository.delete(product_id)
        return {"message": "Product deleted successfully", "status": 200}

    def search_products(self, query: str, page: int, per_page: int):
        results = self.product_repository.search(query, page, per_page)
        return {"products": [{"id": product.id, "name": product.name, "description": product.description, "price": product.price} for product in results], "status": 200}
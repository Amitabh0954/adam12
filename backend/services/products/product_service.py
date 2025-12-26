from repositories.products.product_repository import ProductRepository
from models.product import Product

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, price: float, description: str, category_id: int):
        if not name or price is None or not description or category_id is None:
            return {"message": "All product details are required", "status": 400}

        if price <= 0:
            return {"message": "Price must be a positive number", "status": 400}

        if self.product_repository.find_by_name(name):
            return {"message": "Product name already exists", "status": 400}

        product = Product(id=None, name=name, price=price, description=description, category_id=category_id)
        self.product_repository.save(product)
        return {"message": "Product added successfully", "status": 201, "product": {"id": product.id, "name": product.name, "price": product.price, "description": product.description, "category_id": product.category_id}}
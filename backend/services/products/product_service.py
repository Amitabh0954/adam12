from repositories.products.product_repository import ProductRepository
from models.product import Product

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, data: dict):
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        if not name or not price or not description:
            return {"message": "Name, price, and description are required", "status": 400}

        if price <= 0:
            return {"message": "Price must be a positive number", "status": 400}

        if self.product_repository.find_by_name(name):
            return {"message": "Product name must be unique", "status": 400}

        product = Product(name=name, price=price, description=description)
        self.product_repository.save(product)

        return {"message": "Product added successfully", "status": 201}

    def get_product(self, product_id: int):
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}

        return {"message": "Product retrieved successfully", "status": 200, "product": product.__dict__}

    def get_all_products(self):
        products = self.product_repository.get_all()
        return {"message": "All products retrieved successfully", "status": 200, "products": [product.__dict__ for product in products]}
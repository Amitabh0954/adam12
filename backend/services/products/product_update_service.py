from repositories.products.product_repository import ProductRepository
from typing import Optional

class ProductUpdateService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, name: Optional[str], price: Optional[float], description: Optional[str]):
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}

        if price is not None and price <= 0:
            return {"message": "Price must be a positive number", "status": 400}

        product.name = name if name else product.name
        product.price = price if price is not None else product.price
        product.description = description if description else product.description
        self.product_repository.save(product)
        return {"message": "Product updated successfully", "status": 200, "product": {"id": product.id, "name": product.name, "price": product.price, "description": product.description}}
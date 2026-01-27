# Epic Title: Product Catalog Management

from backend.models.product.product import Product
from backend.repositories.product.product_repository import ProductRepository

class AdminProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository
    
    def update_product(self, product_id: int, name: str, description: str, price: float) -> Product:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product does not exist")
        product.update_product(name, description, price)
        self.product_repository.update_product(product)
        return product
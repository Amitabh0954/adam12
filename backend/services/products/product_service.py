from backend.models.products.product import Product
from backend.repositories.products.product_repository import ProductRepository

product_repository = ProductRepository()

def add_product(product: Product):
    existing_product = product_repository.get_by_name(product.name)
    if existing_product:
        raise ValueError("Product name must be unique")
    product_repository.save(product)
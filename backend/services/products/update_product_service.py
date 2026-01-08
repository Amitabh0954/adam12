from backend.models.products.product_update import ProductUpdate
from backend.repositories.products.product_repository import ProductRepository

product_repository = ProductRepository()

def update_product(product_id: int, product_update: ProductUpdate) -> ProductUpdate:
    product = product_repository.get_by_id(product_id)
    if not product:
        raise ValueError("Product not found")

    if product_update.name and product_repository.get_by_name(product_update.name) and product_update.name != product.name:
        raise ValueError("Product name must be unique")

    product.name = product_update.name if product_update.name else product.name
    product.description = product_update.description
    product.price = product_update.price if product_update.price else product.price

    product_repository.save(product)
    return product
from backend.repositories.products.product_repository import ProductRepository

product_repository = ProductRepository()

def delete_product(product_id: int):
    product = product_repository.get_by_id(product_id)
    if not product:
        raise ValueError("Product not found")
    product_repository.delete(product_id)
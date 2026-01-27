# Epic Title: Product Catalog Management

from backend.models.product.product import Product
from typing import Optional

class ProductRepository:
    def __init__(self):
        # Initialize database connection here
        pass
    
    def add_product(self, product: Product) -> None:
        # logic to add product to the database
        pass
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        # logic to retrieve a product by id
        pass
    
    def get_product_by_name(self, name: str) -> Optional[Product]:
        # logic to retrieve a product by name
        pass
    
    def update_product(self, product: Product) -> None:
        # logic to update the product in the database
        pass

    def delete_product(self, product_id: int) -> None:
        # logic to delete the product from the database
        pass
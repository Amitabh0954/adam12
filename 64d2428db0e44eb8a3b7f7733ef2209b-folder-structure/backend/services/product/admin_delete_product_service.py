# Epic Title: Product Catalog Management

from backend.repositories.product.product_repository import ProductRepository

class AdminDeleteProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository
    
    def delete_product(self, product_id: int) -> bool:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product does not exist")
        
        self.product_repository.delete_product(product_id)
        return True
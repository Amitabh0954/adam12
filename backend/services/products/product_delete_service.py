from repositories.products.product_repository import ProductRepository

class ProductDeleteService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int):
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}
        
        self.product_repository.delete(product_id)
        return {"message": "Product deleted successfully", "status": 200}
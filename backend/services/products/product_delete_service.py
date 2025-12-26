from repositories.products.product_delete_repository import ProductDeleteRepository

class ProductDeleteService:
    def __init__(self):
        self.product_delete_repository = ProductDeleteRepository()

    def delete_product(self, product_id: int):
        product = self.product_delete_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}

        self.product_delete_repository.delete(product_id)
        return {"message": "Product deleted successfully", "status": 200}
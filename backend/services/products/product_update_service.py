from repositories.products.product_update_repository import ProductUpdateRepository

class ProductUpdateService:
    def __init__(self):
        self.product_update_repository = ProductUpdateRepository()

    def update_product(self, product_id: int, data: dict):
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        if not description:
            return {"message": "Description cannot be removed", "status": 400}

        product = self.product_update_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}

        product.update(name=name, price=price, description=description)
        self.product_update_repository.save(product)

        return {"message": "Product updated successfully", "status": 200, "product": product.__dict__}
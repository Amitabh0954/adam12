from repositories.products.product_repository import ProductRepository
from typing import List, Dict

class ProductSearchService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int, per_page: int) -> Dict[str, any]:
        products = self.product_repository.search(query)
        total = len(products)
        start = (page - 1) * per_page
        end = start + per_page
        products_page = products[start:end]
        
        return {
            "message": "Products retrieved successfully",
            "status": 200,
            "products": [{"id": product.id, "name": product.name, "price": product.price, "description": product.description, "category_id": product.category_id} for product in products_page],
            "total": total,
            "page": page,
            "per_page": per_page
        }
from repositories.products.product_search_repository import ProductSearchRepository

class ProductSearchService:
    def __init__(self):
        self.product_search_repository = ProductSearchRepository()

    def search_products(self, query: str, page: int):
        per_page = 10
        results = self.product_search_repository.search_products(query, page, per_page)
        total = self.product_search_repository.total_products(query)

        return {
            "message": "Products retrieved successfully",
            "status": 200,
            "products": [result.__dict__ for result in results],
            "pagination": {
                "total": total,
                "page": page,
                "per_page": per_page
            }
        }
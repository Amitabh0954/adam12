# Epic Title: Product Catalog Management

from backend.repositories.product.product_repository import ProductRepository
from typing import List, Dict

class SearchProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def search_products(self, query: str, page: int = 1, page_size: int = 10) -> List[Dict]:
        results = self.product_repository.search_products(query, page, page_size)
        highlighted_results = self.highlight_search_terms(results, query)
        return highlighted_results

    def highlight_search_terms(self, results: List[Dict], query: str) -> List[Dict]:
        terms = query.split()
        for result in results:
            for term in terms:
                result['name'] = result['name'].replace(term, f"<mark>{term}</mark>")
                result['description'] = result['description'].replace(term, f"<mark>{term}</mark>")
        return results
from typing import List, Dict
from backend.repositories.products.product_repository import ProductRepository

product_repository = ProductRepository()

def search_products(query: str, page: int, page_size: int) -> List[Dict]:
    products = product_repository.search(query)
    start = (page - 1) * page_size
    end = start + page_size
    paginated_products = products[start:end]

    return {"products": [p.dict() for p in paginated_products], "total": len(products), "page": page, "page_size": page_size}
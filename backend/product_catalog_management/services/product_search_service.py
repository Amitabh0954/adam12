from sqlalchemy.orm import Session
from sqlalchemy import or_
from backend.product_catalog_management.models.product import Product
from typing import List, Dict

class ProductSearchService:
    def __init__(self, session: Session):
        self.session = session

    def search_products(self, query: str, page: int = 1, per_page: int = 10) -> Dict[str, any]:
        filters = or_(
            Product.name.like(f"%{query}%"), 
            Product.description.like(f"%{query}%")
        )
        
        products = self.session.query(Product).filter(filters).filter(Product.is_deleted == False)
        
        total_results = products.count()
        paginated_products = products.offset((page - 1) * per_page).limit(per_page).all()
        
        return {
            "page": page,
            "per_page": per_page,
            "total_results": total_results,
            "results": paginated_products
        }

    @staticmethod
    def highlight_search_term(text: str, term: str) -> str:
        return text.replace(term, f"<mark>{term}</mark>")

#### 3. Implement a controller to expose the API for searching products

##### ProductSearchController
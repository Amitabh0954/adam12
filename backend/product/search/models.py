from backend.product.catalog.models import db, Product, Category

class SearchQuery:
    @staticmethod
    def search_products(query: str, page: int = 1, per_page: int = 10):
        search = f"%{query}%"
        products = Product.query.filter(
            Product.name.like(search) |
            Product.description.like(search) |
            Product.categories.any(Category.name.like(search))
        ).filter(Product.is_active == True).paginate(page=page, per_page=per_page, error_out=False)
        
        return products

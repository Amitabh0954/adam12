from models.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []

    def find_by_name(self, name: str) -> Product:
        return next((product for product in self.products if product.name == name), None)
    
    def find_by_id(self, product_id: int) -> Product:
        return next((product for product in self.products if product.id == product_id), None)
    
    def search(self, query: str, page: int, per_page: int) -> dict:
        matched_products = [product for product in self.products if query.lower() in product.name.lower() and not product.is_deleted]
        total_products = len(matched_products)
        start = (page - 1) * per_page
        end = start + per_page
        paginated_products = matched_products[start:end]
        
        results = []
        for product in paginated_products:
            highlighted_name = product.name.replace(query, f'<strong>{query}</strong>', flags=re.IGNORECASE)
            results.append({
                "id": product.id,
                "name": highlighted_name,
                "price": product.price,
                "description": product.description,
                "category_id": product.category_id,
                "created_at": product.created_at,
                "updated_at": product.updated_at
            })
        
        return {
            "products": results,
            "total_products": total_products,
            "page": page,
            "per_page": per_page,
            "query": query
        }

    def save(self, product: Product) -> None:
        self.products.append(product)

    def update(self, product: Product) -> None:
        index = next((i for i, p in enumerate(self.products) if p.id == product.id), None)
        if index is not None:
            self.products[index] = product
    
    def delete(self, product: Product) -> None:
        product.is_deleted = True
        self.update(product)
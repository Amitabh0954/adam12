from backend.product_catalog_management.models.product import Product
from backend.product_catalog_management.schemas.product_schema import ProductSchema
from backend.product_catalog_management.schemas.product_update_schema import ProductUpdateSchema
from backend.product_catalog_management.schemas.product_search_schema import ProductSearchSchema
from sqlalchemy.orm import Session
from marshmallow import ValidationError

class ProductService:
    def __init__(self, session: Session):
        self.session = session

    def add_product(self, data: dict) -> Product:
        try:
            product_data = ProductSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        new_product = Product(**product_data)
        self.session.add(new_product)
        self.session.commit()
        return new_product

    def update_product(self, product_id: int, data: dict) -> Product:
        try:
            update_data = ProductUpdateSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        product = self.session.query(Product).filter_by(id=product_id).first()
        if not product:
            raise ValueError("Product not found")

        for key, value in update_data.items():
            setattr(product, key, value)

        self.session.commit()
        return product

    def delete_product(self, user_id: int, product_id: int) -> None:
        product = self.session.query(Product).filter_by(id=product_id).first()
        if not product:
            raise ValueError("Product not found")

        self.session.delete(product)
        self.session.commit()

    def search_products(self, query: dict):
        try:
            search_data = ProductSearchSchema().load(query)
        except ValidationError as err:
            raise ValueError(f"Invalid search data: {err.messages}")

        page = search_data['page']
        size = search_data['size']
        search_query = search_data['query']
        
        products = self.session.query(Product).filter(
            Product.name.ilike(f"%{search_query}%") | 
            Product.description.ilike(f"%{search_query}%")
        ).limit(size).offset((page - 1) * size).all()

        return products

#### 4. Implement the product search controller
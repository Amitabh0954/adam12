from backend.product_catalog_management.models.product import Product
from backend.product_catalog_management.schemas.product_schema import ProductSchema
from backend.product_catalog_management.schemas.product_update_schema import ProductUpdateSchema
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

#### 4. Add the product update route and controller method
from backend.product_catalog_management.models.product import Product
from backend.product_catalog_management.schemas.product_schema import ProductSchema
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

#### 4. Implement the product management controller
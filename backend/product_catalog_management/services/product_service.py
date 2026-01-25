from sqlalchemy.orm import Session
from backend.product_catalog_management.models.product import Product
from backend.product_catalog_management.schemas.product_schema import ProductUpdateSchema
from marshmallow import ValidationError

class ProductService:
    def __init__(self, session: Session):
        self.session = session

    def update_product(self, product_id: int, data: dict) -> Product:
        product = self.session.query(Product).get(product_id)
        if not product:
            raise ValueError("Product not found")

        try:
            valid_data = ProductUpdateSchema().load(data, partial=True)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        for key, value in valid_data.items():
            setattr(product, key, value)

        self.session.commit()
        return product

##### ProductUpdateSchema
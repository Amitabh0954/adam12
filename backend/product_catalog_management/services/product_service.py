from sqlalchemy.orm import Session
from backend.product_catalog_management.models.product import Product
from backend.product_catalog_management.schemas.product_schema import ProductSchema
from marshmallow import ValidationError

class ProductService:
    def __init__(self, session: Session):
        self.session = session

    def add_product(self, data: dict) -> Product:
        try:
            valid_data = ProductSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        if self.session.query(Product).filter_by(name=valid_data['name']).first():
            raise ValueError("Product name already exists")

        product = Product(**valid_data)
        self.session.add(product)
        self.session.commit()
        return product

#### 3. Implement a controller to expose the API for adding new products

##### ProductController
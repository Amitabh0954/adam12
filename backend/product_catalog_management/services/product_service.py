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

        existing_product = self.session.query(Product).filter_by(name=valid_data['name']).first()
        if existing_product:
            raise ValueError("Product name already exists")

        new_product = Product(**valid_data)
        self.session.add(new_product)
        self.session.commit()

        return new_product

    def update_product(self, product_id: int, data: dict) -> Product:
        product = self.session.query(Product).get(product_id)
        if not product:
            raise ValueError("Product not found")

        try:
            valid_data = ProductSchema().load(data, partial=True)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        # Ensure prices are numeric and description cannot be removed
        if 'price' in valid_data and not isinstance(valid_data['price'], (int, float)):
            raise ValueError("Price must be a numeric value")

        if 'description' in valid_data and not valid_data['description']:
            raise ValueError("Description cannot be removed")

        for key, value in valid_data.items():
            setattr(product, key, value)

        self.session.commit()

        return product

#### 3. Implement a controller to expose the API for updating products

##### ProductController
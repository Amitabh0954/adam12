from backend.product_catalog_management.models.product import Product
from backend.product_catalog_management.schemas.product_schema import ProductSchema
from backend.product_catalog_management.schemas.product_update_schema import ProductUpdateSchema
from sqlalchemy.orm import Session
from marshmallow import ValidationError

def is_admin(user_id: int) -> bool:
    # Placeholder check. Implement actual admin verification here.
    return user_id == 1  # Example hardcoded admin ID

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
        if not is_admin(user_id):
            raise PermissionError("Only admins can delete products")

        product = self.session.query(Product).filter_by(id=product_id).first()
        if not product:
            raise ValueError("Product not found")

        self.session.delete(product)
        self.session.commit()

#### 4. Implement the controller to handle delete requests
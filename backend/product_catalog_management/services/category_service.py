from sqlalchemy.orm import Session
from backend.product_catalog_management.models.category import Category
from backend.product_catalog_management.schemas.category_schema import CategorySchema
from marshmallow import ValidationError

class CategoryService:
    def __init__(self, session: Session):
        self.session = session

    def create_category(self, data: dict) -> Category:
        try:
            category_data = CategorySchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        new_category = Category(**category_data)
        self.session.add(new_category)
        self.session.commit()
        return new_category

    def update_category(self, category_id: int, data: dict) -> Category:
        try:
            update_data = CategorySchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        category = self.session.query(Category).filter_by(id=category_id).first()
        if not category:
            raise ValueError("Category not found")

        for key, value in update_data.items():
            setattr(category, key, value)

        self.session.commit()
        return category

    def delete_category(self, category_id: int):
        category = self.session.query(Category).filter_by(id=category_id).first()
        if not category:
            raise ValueError("Category not found")

        self.session.delete(category)
        self.session.commit()

#### 5. Implement the category management controller
from marshmallow import Schema, fields, validates, ValidationError

class ProductUpdateSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    price = fields.Float()

    @validates('price')
    def validate_price(self, value: float) -> None:
        if value <= 0:
            raise ValidationError("Price must be a positive number")

    @validates('description')
    def validate_description(self, value: str) -> None:
        if not value:
            raise ValidationError("Description cannot be empty")

#### 3. Implement a controller to expose the API endpoints for updating products

##### ProductController
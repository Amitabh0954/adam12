from marshmallow import Schema, fields, validates, ValidationError

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    is_available = fields.Bool()

    @validates('name')
    def validate_name(self, value: str) -> None:
        if not value:
            raise ValidationError("Product name cannot be empty")

    @validates('price')
    def validate_price(self, value: float) -> None:
        if value <= 0:
            raise ValidationError("Price must be a positive number")

    @validates('description')
    def validate_description(self, value: str) -> None:
        if not value:
            raise ValidationError("Description cannot be empty")

#### 4. Update routes to include the new product addition endpoint

##### Updated Routes
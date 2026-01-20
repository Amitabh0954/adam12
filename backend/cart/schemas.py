from marshmallow import Schema, fields, validate

class CartItemSchema(Schema):
    id = fields.Int(dump_only=True)
    cart_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True, validate=validate.Range(min=1))

class CartSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    items = fields.List(fields.Nested(CartItemSchema), dump_only=True)
    created_at = fields.DateTime(dump_only=True)

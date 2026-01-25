from marshmallow import Schema, fields

class ShoppingCartItemSchema(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class ShoppingCartSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    items = fields.List(fields.Nested(ShoppingCartItemSchema), dump_only=True)

#### 3. Implement shopping cart services
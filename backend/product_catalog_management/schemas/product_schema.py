from marshmallow import Schema, fields, validate

class ProductSchema(Schema):
    name = fields.String(required=True, validate=[validate.Length(min=1, max=255)])
    price = fields.Float(required=True, validate=[validate.Range(min=0.01)])
    description = fields.String(required=True, validate=[validate.Length(min=1)])

#### 3. Implement the product management service
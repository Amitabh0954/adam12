from marshmallow import Schema, fields, validate

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
    price = fields.Float(required=True, validate=validate.Range(min=0.01))
    description = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
    product_id = fields.Int(required=True)

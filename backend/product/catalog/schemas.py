from marshmallow import Schema, fields, validate

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
    price = fields.Float(required=True, validate=validate.Range(min=0.01))
    description = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    is_active = fields.Bool(dump_only=True)

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
    parent_id = fields.Int(allow_none=True)
    product_id = fields.Int(required=True)

class UpdateProductSchema(Schema):
    name = fields.Str(validate=validate.Length(max=100))
    price = fields.Float(validate=validate.Range(min=0.01))
    description = fields.Str()

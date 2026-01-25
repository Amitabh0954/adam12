from marshmallow import Schema, fields

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    parent_id = fields.Int(allow_none=True)

#### 4. Implement category management service
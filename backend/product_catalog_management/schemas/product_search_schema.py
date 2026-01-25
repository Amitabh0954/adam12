from marshmallow import Schema, fields

class ProductSearchSchema(Schema):
    query = fields.String(required=True)
    page = fields.Int(missing=1)
    size = fields.Int(missing=10)

#### 3. Implement the search service
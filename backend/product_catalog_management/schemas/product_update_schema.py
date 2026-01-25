from marshmallow import Schema, fields, validate

class ProductUpdateSchema(Schema):
    name = fields.String(validate=[validate.Length(min=1, max=255)], required=True)
    price = fields.Float(validate=[validate.Range(min=0.01)], required=True)
    description = fields.String(validate=[validate.Length(min=1)], required=True)

#### 3. Update `ProductService` to handle product updates
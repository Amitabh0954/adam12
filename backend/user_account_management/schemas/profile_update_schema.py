from marshmallow import Schema, fields, validate

class ProfileUpdateSchema(Schema):
    email = fields.Email(required=True, validate=[validate.Length(min=5, max=255)])
    first_name = fields.String(validate=[validate.Length(max=100)], allow_none=True)
    last_name = fields.String(validate=[validate.Length(max=100)], allow_none=True)
    phone_number = fields.String(validate=[validate.Length(max=20)], allow_none=True)
    address = fields.String(validate=[validate.Length(max=500)], allow_none=True)

#### 3. Implement the profile management service
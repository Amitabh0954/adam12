from marshmallow import Schema, fields, validate

class PasswordResetRequestSchema(Schema):
    email = fields.Email(required=True, validate=[validate.Length(min=5, max=255)])

class PasswordResetSchema(Schema):
    token = fields.String(required=True)
    new_password = fields.String(required=True, validate=[validate.Length(min=8)])

#### 3. Update `UserService` to handle password recovery logic
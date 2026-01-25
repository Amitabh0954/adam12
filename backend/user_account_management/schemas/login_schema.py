from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    email = fields.Email(required=True, validate=[validate.Length(min=5, max=255)])
    password = fields.String(required=True, validate=[validate.Length(min=8)])

#### 3. Update `UserService` to handle login logic
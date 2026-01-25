from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    email = fields.Email(required=True, validate=[validate.Length(min=5, max=255)])
    password = fields.String(required=True, validate=[validate.Length(min=8)])

#### 3. Create `services/user_service.py` for the business logic of user account management
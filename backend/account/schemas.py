from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True, validate=validate.Length(max=120))
    password = fields.Str(load_only=True, required=True, validate=[validate.Length(min=8), validate.Regexp(
        regex='(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)',
        error='Password must contain at least one uppercase letter, one lowercase letter, and one number'
    )])
    created_at = fields.DateTime(dump_only=True)

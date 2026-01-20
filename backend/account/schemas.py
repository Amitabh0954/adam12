from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True, validate=validate.Length(max=120))
    password = fields.Str(load_only=True, required=True, validate=[validate.Length(min=8), validate.Regexp(
        regex='(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)',
        error='Password must contain at least one uppercase letter, one lowercase letter, and one number'
    )])
    created_at = fields.DateTime(dump_only=True)

class LoginAttemptSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    attempted_at = fields.DateTime(dump_only=True)
    success = fields.Bool(dump_only=True)

class PasswordResetTokenSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    token = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    expiry_date = fields.DateTime(dump_only=True)
    is_used = fields.Bool(dump_only=True)

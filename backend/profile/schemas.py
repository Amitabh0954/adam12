from marshmallow import Schema, fields, validate

class ProfileSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    first_name = fields.Str(validate=validate.Length(max=50))
    last_name = fields.Str(validate=validate.Length(max=50))
    preferences = fields.Dict()
    updated_at = fields.DateTime(dump_only=True)

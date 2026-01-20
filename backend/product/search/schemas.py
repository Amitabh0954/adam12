from marshmallow import Schema, fields

class SearchResultSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Float()
    description = fields.Str()

class PageSchema(Schema):
    total = fields.Int()
    pages = fields.Int()
    page = fields.Int()
    per_page = fields.Int()
    items = fields.List(fields.Nested(SearchResultSchema))

from marshmallow import Schema, fields

class CarSchema(Schema):
    id = fields.Integer(dump_only=True)
    make = fields.Str(required=True)
    model = fields.Str(required=True)
    year = fields.Integer(required=True)
    value = fields.Float(required=True)
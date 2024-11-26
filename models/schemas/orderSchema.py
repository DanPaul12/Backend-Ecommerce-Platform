from marshmallow import fields, validate
from schema import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=True)
    customer_id = fields.Integer(required=True)
    products = fields.Nested('ProductSchema', many=True)


order_schema = OrderSchema()
orders_schema = OrderSchema(many = True)
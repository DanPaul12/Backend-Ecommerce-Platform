from marshmallow import fields, validate
from schema import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=True)
    customer_id = fields.Integer(required=True)
    products = fields.Nested('ProductSchema', many=True)
      #why are these schemas passed in as strings, and why not instantiated

order_schema = OrderSchema()
orders_schema = OrderSchema(many = True)

class OrderSchemaCustomer(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=True)
    products = fields.Nested('ProductSchema', many=True)
    customer = fields.Nested('CustomerSchema')

orders_schema_customer = OrderSchemaCustomer()
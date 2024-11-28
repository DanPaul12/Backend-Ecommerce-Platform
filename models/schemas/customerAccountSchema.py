from schema import ma
from marshmallow import fields

class customerAccount(ma.Schema):
    id = fields.Integer(required=False)
    username = fields.String(required=True)
    password = fields.String(required=True)
    customer = fields.Nested('CustomerSchema')

customer_account_schema = customerAccount()
customer_accounts_schema = customerAccount(many=True)
from models.schemas.customerAccountSchema import customer_accounts_schema, customer_account_schema
from services import customerAccountService
from flask import request, jsonify

def find_all():
    customer_accounts = customerAccountService.find_all()
    return customer_accounts_schema.jsonify(customer_accounts), 200

def login_customer():
    customer = request.json
    user = customerAccountService.login_customer(customer['username'], customer['password'])
    if user:
        return jsonify(user), 200
    else:
        resp={
            "message":"failure"
        }
        return jsonify(resp), 400

def find_account(id):
    account = customerAccountService.find_account(id)
    return customer_account_schema.jsonify(account)
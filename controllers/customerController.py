from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from models.schemas.customerAccountSchema import customer_account_schema
from services import customerService, customerAccountService
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer_save = customerService.save(customer_data)
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else:
        return jsonify({'message':'fallback triggered'}, {'body':customer_data}), 400

#@cache.cached(timeout=60) 
@token_required   
def find_all():
    customers = customerService.find_all()
    return customers_schema.jsonify(customers), 200


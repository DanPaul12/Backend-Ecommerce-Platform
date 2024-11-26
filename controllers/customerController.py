from flask import request, jsonify
from models.schemas.customerSchema import customer_schema
from services import customerService
from marshmallow import ValidationError

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer_save = customerService.save(customer_data)
    return customer_schema.jsonify(customer_save), 201
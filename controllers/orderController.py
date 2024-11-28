from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema_customer
from services import orderService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    try:
        order_save = orderService.save(order_data)
        return order_schema.jsonify(order_save), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
def find_by_id(id):
    order = orderService.find_by_id(id)
    return orders_schema_customer.jsonify(order)
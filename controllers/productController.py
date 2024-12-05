from flask import request, jsonify
from models.schemas.productSchema import product_schema
from services import productService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    try:
        product_save = productService.save(product_data)
        return product_schema.jsonify(product_save), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
def update(id):
    new_data = product_schema.load(request.json)
    return productService.update_product(id, new_data)

def delete(id):
    return productService.delete_product(id)

def find(id):
    product = productService.find_product(id)
    return product_schema.jsonify(product)
    
from flask import Blueprint
from controllers.customerController import save, find_all, find_customer, update_customer, delete_customer

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/<int:id>', methods=['GET'])(find_customer)
customer_blueprint.route('/<int:id>', methods=['PUT'])(update_customer)
customer_blueprint.route('/<int:id>', methods=['DELETE'])(delete_customer)
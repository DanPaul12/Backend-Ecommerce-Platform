from flask import Blueprint
from controllers.customerController import save

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
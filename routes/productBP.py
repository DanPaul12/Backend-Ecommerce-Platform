from flask import Blueprint
from controllers.productController import save, update

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/<int:id>', methods=['PUT'])(update)
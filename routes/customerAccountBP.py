from flask import Blueprint
from controllers.customerAccountController import find_all, login_customer, find_account

customer_account_blueprint = Blueprint('customer_account_bp', __name__)  #what do these arguments do
customer_account_blueprint.route('/', methods=['GET'])(find_all)
customer_account_blueprint.route('/login', methods=['POST'])(login_customer)
customer_account_blueprint.route('/<int:id>', methods=['GET'])(find_account)
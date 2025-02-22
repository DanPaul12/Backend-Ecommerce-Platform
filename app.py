from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from caching import cache
from sqlalchemy.orm import Session
from flask_cors import CORS
from werkzeug.security import generate_password_hash
from flask_swagger_ui import get_swaggerui_blueprint

from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.order import Order
from models.product import Product
from models.role import Role
from models.customerManagementRole import CustomerManagementRole
from models.orderProduct import order_product

from routes.customerBP import customer_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.customerAccountBP import customer_account_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': 'E-Commerce API'}
)


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    CORS(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(customer_account_blueprint, url_prefix='/accounts')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

def configure_rate_limit():
    limiter.limit('100 per day')(customer_blueprint)

def init_customers_info_data():
    with Session(db.engine) as session:
        with session.begin():
            customers = [
                Customer(name='Cus One', email='cus1@gmail.com', phone='8057893487'),
                Customer(name='Cus two', email='cus2@gmail.com', phone='8057893487'),
                Customer(name='Cus three', email='cus3@gmail.com', phone='8057893487')
            ] 

            customerAccounts = [
                CustomerAccount(username= 'ctm1', password= generate_password_hash('password1'), customer_id=4),
                CustomerAccount(username= 'ctm2', password= generate_password_hash('password2'), customer_id=5),
                CustomerAccount(username= 'ctm3', password= generate_password_hash('password3'), customer_id=6),
            ]

            session.add_all(customers)
            session.add_all(customerAccounts)

def init_roles_data():
    with Session(db.engine) as session:
        with session.begin():
            roles = [
                Role(role_name='admin'),
                Role(role_name='user'),
                Role(role_name='guest'),
            ]
            session.add_all(roles)

def init_roles_customers_data():
    with Session(db.engine) as session:
        with session.begin():
            roles_customers=[
                CustomerManagementRole(customer_management_id=1, role_id=1),
                CustomerManagementRole(customer_management_id=2, role_id=2),
                CustomerManagementRole(customer_management_id=2, role_id=3),
            ]
            session.add_all(roles_customers)
           
app = create_app('DevelopmentConfig')
blue_print_config(app)
configure_rate_limit()

with app.app_context():
    db.create_all()

# if __name__ == '__main__':
#     app = create_app('DevelopmentConfig')

#     blue_print_config(app)
#     configure_rate_limit()
    

#     with app.app_context():  
#         #db.drop_all()
#         db.create_all()
#         #init_roles_data()
#         #init_customers_info_data()
#         #init_roles_customers_data()

#     app.run(debug=True)

    
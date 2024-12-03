from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from models.customerAccount import CustomerAccount
from circuitbreaker import circuit
from sqlalchemy import select
from utils.util import encode_token
from werkzeug.security import check_password_hash

def find_all():                #what kind of join is this
    query = select(CustomerAccount).join(Customer).where(Customer.id == CustomerAccount.customer_id)
    customer_accounts = db.session.execute(query).scalars().all()
    return customer_accounts


def login_customer(username, password):
    customer = db.session.execute(select(CustomerAccount).where(CustomerAccount.username == username, CustomerAccount.password == password)).scalar_one_or_none()
    role_names = [role.role_name for role in customer.roles]
    if customer:
        #if check_password_hash(customer.password, password):
            auth_token = encode_token(customer.id, role_names)
            resp = {
                "status":"success",
                "message": "logged in",
                "auth_token":auth_token
            }
            return resp
        #else:
         #   return None
    else:
        return None
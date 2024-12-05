from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from models.customerAccount import CustomerAccount
from circuitbreaker import circuit
from sqlalchemy import select
from utils.util import encode_token
from werkzeug.security import check_password_hash
from flask import jsonify

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
    
def find_account(id):
    query = select(CustomerAccount).where(CustomerAccount.id == id)
    account = db.session.execute(query).scalar_one_or_none()
    return account

def update_account(id, new_data):
    try:
        with Session(db.engine) as session:
                with session.begin():
                    account = session.query(CustomerAccount).filter_by(id=id).first()
                    if not account:
                        return jsonify({'message':'account not found'}), 404
                    account.username = new_data['username']
                    account.password = new_data['password']
                    session.commit()
                    return jsonify({'message':'Account updated'}), 201
    except Exception as e: 
        return {'message': 'An error occurred while updating the account', 'error': str(e)}, 500
    
def delete_account(id):
     with Session(db.engine) as session:
            with session.begin():
                account = session.query(CustomerAccount).filter_by(id=id).first()
                if not account:
                    return {'message': 'account not found'}, 404
                session.delete(account)
                session.commit()
                return jsonify({'message':'account deleted'}), 201
                
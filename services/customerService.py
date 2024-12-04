from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from models.customerAccount import CustomerAccount
from utils.util import encode_token
from circuitbreaker import circuit
from sqlalchemy import select

def fallback_func(customer):
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_func)
def save(customer_data):
    with Session(db.engine) as session:
        try:
            if customer_data['name']== 'Failure':
                raise Exception('Failure condition triggered')
            
            with session.begin():
                new_customer = Customer(name=customer_data['name'], email = customer_data['email'], phone =customer_data['phone'])
                session.add(new_customer)
                session.commit()
            session.refresh(new_customer)
            return new_customer
        
        except Exception as e:
            raise e

def find_all():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers

def find_one(id):
    query = select(Customer).where(Customer.id == id)
    customer = db.session.execute(query).scalar_one_or_none()
    return customer



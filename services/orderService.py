from sqlalchemy.orm import Session
from database import db
from models.product import Product
from models.order import Order
from models.customer import Customer
from circuitbreaker import circuit
from sqlalchemy import select

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            
            product_ids = [product['id'] for product in order_data['products']]
            products = session.execute(select(Product).where(Product.id.in_(product_ids))).scalars().all()

            customer_id = order_data['customer_id']
            customer = session.execute(select(Customer).where(Customer.id==customer_id)).scalars().first()

            if len(products) != len(product_ids):
                raise ValueError('one or more products do not exist')

            if not customer:
                raise ValueError('no customer')

            new_order = Order(date=order_data['date'], customer_id=order_data['customer_id'], products=products)
            session.add(new_order)
            session.flush()
            session.commit()
        
        session.refresh(new_order)

        for product in new_order.products:
            session.refresh(product)

        return new_order
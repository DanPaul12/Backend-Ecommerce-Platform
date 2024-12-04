from sqlalchemy.orm import Session
from database import db
from models.product import Product
from flask import jsonify
from circuitbreaker import circuit
from sqlalchemy import select


def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product
    
def update_product(id, new_data):
    try:
        with Session(db.engine) as session:
            with session.begin():
                query = select(Product).where(Product.id == id)
                product = db.session.execute(query).scalar_one_or_none()
                product.name = new_data['name']
                product.price = new_data['price']
                session.commit()
                return jsonify({'message':'product updated'}), 201
    except Exception as e:
        session.rollback()  
        return {'message': 'An error occurred while updating the product', 'error': str(e)}, 500
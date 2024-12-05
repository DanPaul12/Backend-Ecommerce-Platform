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
    
def find_product(id):
    with Session(db.engine) as session:   #when to use this vs when not to use this vs (find all)
        with session.begin():
            query = select(Product).where(Product.id==id)
            product = db.session.execute(query).scalar_one_or_none()
            if product == {}:
                return jsonify({'message': 'Product not found'}), 404
            return product
        
def find_all():
    query = select(Product)    
    products = db.session.execute(query).scalars().all()
    return products
    
def update_product(id, new_data):
    try:
        with Session(db.engine) as session:
            with session.begin():
                product = session.query(Product).filter_by(id=id).first()
                print(product)
                if not product:
                    return {'message': 'Product not found'}, 404
                print(new_data)
                product.name = new_data['name']
                product.price = new_data['price']
                session.commit()
                return jsonify({'message':'product updated'}), 201
    except Exception as e: 
        return {'message': 'An error occurred while updating the product', 'error': str(e)}, 500
    
def delete_product(id):
    with Session(db.engine) as session:
            with session.begin():
                product = session.query(Product).filter_by(id=id).first()
                if not product:
                    return {'message': 'Product not found'}, 404
                session.delete(product)
                session.commit()
                return jsonify({'message':'product deleted'}), 201
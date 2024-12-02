from datetime import timedelta, datetime
import jwt
import os
from dotenv import load_dotenv
from flask import request, jsonify, current_app
from functools import wraps

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')


def encode_token(user_id,role_names):
    payload={
        'exp': int((datetime.now() + timedelta(days=1)).timestamp()),  # Expiration time
        'iat': int(datetime.now().timestamp()), 
        'sub':user_id,
        'roles': role_names
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    print(SECRET_KEY)
    print('token sent to postman', token)
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=None
        if 'Authorization' in request.headers:
            print('authorization header received', request.headers.get('Authorization'))
            try:
                token = request.headers['Authorization'].split(' ')[1]
                print('Token received from postman:', token)
                #print(SECRET_KEY)
                payload = jwt.decode(token, SECRET_KEY, algorithm='HS256')
                #payload = jwt.decode(token, options={'verify_signature': False})
                print('decoded payload without signature verification', payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message':'token expired'})
            except jwt.InvalidTokenError:
                return jsonify({'message':"invalid token"})
        if not token:
            return jsonify({'message':'token missing'})
        
        return f(*args, **kwargs)
    
    return decorated

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(' ')[1]
            if not token:
                return jsonify({'message':'token is missing'}), 401
            
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithm='HS256')
            except jwt.ExpiredSignatureError:
                return jsonify({'message':'expired token'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message':'invalid token'}), 400
            
            roles = payload['roles']

            if role not in roles:
                return jsonify({'message':'user doesnt have role'}), 403
            
            return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator
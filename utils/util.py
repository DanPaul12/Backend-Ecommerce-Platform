from datetime import timedelta, datetime
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def encode_token(user_id):
    payload={
        'exp': datetime.now() + timedelta(days=0, hours=1 ),
        'iat': datetime.now(),
        'sub':user_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
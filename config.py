import os
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:thegoblet2@localhost/advanced_e_commerce_db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
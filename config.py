import os
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://example_sum_postgres_3qkn_user:nSkwUR0ygS2dEEWA09qgGV9jBApRe8To@dpg-ctd3aijqf0us73bk5080-a.oregon-postgres.render.com/example_sum_postgres_3qkn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
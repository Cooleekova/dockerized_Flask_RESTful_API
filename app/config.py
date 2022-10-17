import os

user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')
database = os.environ.get('DATABASE')


POSTGRES_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
SALT = 'my_sJHLHLHKL_)jzekehckiuper_s!alt_#4$4344'

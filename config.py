DEBUG = True

USERNAME = 'postgres'
PASSWORD = 'postgres'
SERVER = 'localhost'
PORT = '5432'
DB = 'tech_evolution'

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

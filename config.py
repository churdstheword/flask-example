import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE = os.environ.get('DATABASE')
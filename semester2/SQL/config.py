import os 
from dotenv import load_dotenv

load_dotenv()

class Config():
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    database = os.getenv('DATABASE')
    password = os.getenv('PASSWORD')
    user = os.getenv('USER')
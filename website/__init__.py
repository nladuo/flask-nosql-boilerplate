from flask import Flask
from flask_pymongo import PyMongo
from redis import Redis


app = Flask(__name__)
app.config['MONGO_DBNAME'] = "test_db"
app.config['MONGO_HOST'] = "localhost"
app.config['MONGO_PORT'] = "27017"


mongo = PyMongo(app)
redis = Redis()

from .routes import *

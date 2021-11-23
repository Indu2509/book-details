from flask import Flask
from applogging.config import ProductionConfig,StaggingConfig,Config
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo


app = Flask(__name__)


CORS(app)

if app.config["ENV"] == "prod":
     app.config.from_object(ProductionConfig)
elif app.config["ENV"] == "stage":
    app.config.from_object(StaggingConfig)
else:
    app.config.from_object(Config)



from app import serviceapi

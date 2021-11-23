from bson.objectid import ObjectId
from pymongo import MongoClient
from app import app
import logging
import json
from flask import jsonify, request
from flask_jwt_extended import (
    JWTManager

)
import json
import excel2json

import os
filePath = 'app/books-2.json'

if os.path.exists(filePath):
    os.remove(filePath)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)


@app.route('/getRowsdata')
def getRowsdata():
    rows = request.args.get('row')
    rows =int(rows)
    excel2json.convert_from_file('app/books.xlsx')

    jsonFile = open("app/books-2.json",)
    data = json.load(jsonFile)
    print(data[0:rows])
    return jsonify(data=data[0:rows])

@app.route('/getRequestedKeydata')
def getRequestedKeydata():
    keyvalue = request.args.get('KeyValue')
    keyvalue = json.loads(keyvalue)
    key =list(keyvalue.keys())
    value = keyvalue[key[0]]
    excel2json.convert_from_file('app/books.xlsx')
    jsonFile = open("app/books-2.json",)
    data = json.load(jsonFile)
    if(data[0].get(key[0])):
        for x in data:
            if x[key[0]] == value:
                return x
    else:
        return "Key does not exist"


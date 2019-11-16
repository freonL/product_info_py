import os
from flask import Flask, Response, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv

from models import JSONEncoder
load_dotenv()
app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client.product_info

from bson.objectid import ObjectId

@app.route('/products',methods = ['GET'])
def get_list():
    collection = db.products
    docs = []

    for doc in collection.find():
        docs.append(doc)

    return Response(JSONEncoder().encode(docs), mimetype='application/json', status=200)

@app.route('/products',methods = ['POST'])
def create():
    req = request.get_json()

    return jsonify({}), 200

@app.route('/products/<id>',methods = ['GET'])
def get_detail(id):
    doc = db.products.find_one({"_id": ObjectId(id)})
    return Response(JSONEncoder().encode(doc), mimetype='application/json', status=200)

@app.route('/products/<id>',methods = ['PATCH'])
def update(id):

    req = request.get_json()

    return jsonify({}), 200

@app.route('/products/<id>',methods = ['DELETE'])
def delete(id):
    pass

if __name__== '__main__':
    app.run(debug=True, port=5000)
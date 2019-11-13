import os
from flask import Flask, Response, jsonify, request
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
from bson.json_util import dumps
from bson.objectid import ObjectId
load_dotenv()
app = Flask(__name__)
app.config['MONGODB_DB'] = os.getenv("MONGODB_DB")
app.config['MONGODB_HOST'] =  os.getenv("MONGODB_HOST")
app.config['MONGODB_PORT'] = int(os.getenv("MONGODB_PORT"))
app.config['MONGODB_USERNAME'] = os.getenv("MONGODB_USERNAME")
app.config['MONGODB_PASSWORD'] = os.getenv("MONGODB_PASSWORD")
db = MongoEngine(app)


from models.products import Products

@app.route('/products',methods = ['GET'])
def get_list():
    docs = Products.objects()
    return jsonify(docs), 200

@app.route('/products',methods = ['POST'])
def create():

    pass

@app.route('/products/<id>',methods = ['GET'])
def get_detail(id):

    docs = Products.objects(id=id)
    return jsonify(docs), 200

@app.route('/products/<id>',methods = ['PUT'])
def update(id):
    pass

@app.route('/products/<id>',methods = ['DELETE'])
def delete(id):
    pass

if __name__== '__main__':
    app.run(debug=True, port=5000)
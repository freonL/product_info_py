import os
from flask import Flask, Response, jsonify, request
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db':os.getenv("MONGODB_DB"),
    'host':os.getenv("MONGODB_URI")
}
db = MongoEngine(app)


from models.products import Products

@app.route('/products',methods = ['GET'])
def get_list():
    docs = Products.objects()
    return jsonify(docs), 200

@app.route('/products',methods = ['POST'])
def create():
    req = request.get_json()
    doc = Products.from_json(req)
    doc.save()
    return jsonify(doc), 200

@app.route('/products/<id>',methods = ['GET'])
def get_detail(id):
    doc = Products.objects(id=id)
    return jsonify(doc), 200

@app.route('/products/<id>',methods = ['PATCH'])
def update(id):
    doc = Products.objects(id=id)
    req = request.get_json()
    print(req)
    for r in req:
        print(r,req[r])
    return jsonify(doc), 200

@app.route('/products/<id>',methods = ['DELETE'])
def delete(id):
    pass

if __name__== '__main__':
    app.run(debug=True, port=5000)
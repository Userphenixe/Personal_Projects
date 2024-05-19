from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

@app.route('/products', methods =['GET'])
def get_products():
    if request.method == 'GET':
        return jsonify(products)

@app.route('/products/<id>', methods =['GET'])
def get_products_by_ids(id):
    id = int(id)
    for product in products:
        if product['id'] == id:
            return jsonify(product)
        else:
            pass

@app.route('/products', methods = ['POST'])
def add_product():
    products.append(request.get_json())
    return '', 201

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    id = int(id)
    updated_product = json.loads(request.data)
    for product in products:
        if product['id'] == id:
            for key, value in updated_product.items():
                product[key] = value
            break
    return '', 204

@app.route('/products/<id>', methods = ['DELETE'])
def delete_product(id):
    id = int(id)
    for product in products:
        if product['id'] == id:
            products.remove(product)
        else:
            pass


app.run(port=5000,debug=True)

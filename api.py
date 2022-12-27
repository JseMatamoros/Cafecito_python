# API - Una api es un lugar para disponibilizar recursos y o funcionalidades

# 1 Objetivo - Crear una API que facilita la consulta, creacion, edicion y eliminacion de productos

# 2 URL BASE - localhost:5000

# 3 Endpoints - 
    # - localhost/productos(POST)
    # - localhost/productos(GET)
    # - localhost/productos/id (GET)
    # - localhost/productos/id (PUT)
    # - localhost/productos/id (DELETE)
    
from flask import Flask, jsonify, request
api = Flask(__name__)

productos = [
    {
        'id': 1,
        'nombre': 'Donuts',
        'descripcion': 'rellenas de chocolate',
        'valor': 1990
    },
    {
        'id': 2,
        'nombre': 'Cafe Fuerte',
        'descripcion': 'Con granos seleccionados, tostado y molido.',
        'valor': 1600
    },
    {
        'id': 3,
        'nombre': 'Torta',
        'descripcion': 'De chocolate y manjar',
        'valor': 2500
    }
]

# GET
@api.route('/productos',methods=['GET'])
def mostrar_productos():
    return jsonify(productos)

# GET (id)
@api.route('/productos/<int:id>',methods=['GET'])
def mostrar_producto_con_id(id):
    for producto in productos:
        if producto.get('id') == id:
            return jsonify(producto)

# POST
@api.route('/productos',methods=['POST'])
def agregar_producto():
    nuevo_producto = request.get_json()
    productos.append(nuevo_producto)
    return jsonify(productos)

# PUT
@api.route('/productos/<int:id>', methods=['PUT'])
def editar_producto_id(id):
    producto_editado = request.get_json()
    for indice,producto in enumerate(productos):
        if producto.get('id') == id:
            productos[indice].update(producto_editado)
            return jsonify(productos[indice])

# DELETE
@api.route('/productos/<int:id>',methods=['DELETE'])
def eliminar_producto(id):
    for indice,producto in enumerate(productos):
        if producto.get('id') == id:
            del productos[indice]
            return jsonify(productos)

api.run(port=5000, host='localhost', debug=True)
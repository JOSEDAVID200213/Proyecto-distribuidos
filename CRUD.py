from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

app = Flask(__name__)

uri = "mongodb+srv://jmunoz6:Rpg200213@cluster0.w3e20jx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Lo ideal es que la url no esté al lado del resto del código, ya que así se evitan inyecciones hackers.
client = MongoClient(uri, server_api=ServerApi('1'))

# Verifica si la conexión se estableció correctamente
try:
    client.admin.command('ping')
    print("Conexión a MongoDB Atlas establecida correctamente.")
    db = client['Distribuidos']
    coleccion_productos = db.productos
except Exception as e:
    print(f"Error al conectar a MongoDB Atlas: {e}")

def producto_a_json(producto):
    return {
        'producto_id': producto['producto_id'],
        'nombre': producto['nombre'],
        'precio': producto['precio']
    }

@app.errorhandler(404)
def not_found(error):
    return jsonify({'mensaje': 'Producto no encontrado'}), 404

# Ruta para obtener todos los documentos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    productos = coleccion_productos.find()
    resultado = [producto_a_json(producto) for producto in productos]
    return jsonify({'productos': resultado})

# Ruta para obtener un documento por su ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto_por_id(producto_id):
    producto = coleccion_productos.find_one({'producto_id': producto_id})
    if producto:
        return jsonify(producto_a_json(producto))
    else:
        return not_found(None)

# Ruta para crear un nuevo documento
@app.route('/productos', methods=['POST'])
def crear_producto():
    producto_id = request.json['producto_id']
    nombre = request.json['nombre']
    precio = request.json['precio']
    nuevo_producto = {
        'producto_id': producto_id,
        'nombre': nombre,
        'precio': precio
    }
    resultado = coleccion_productos.insert_one(nuevo_producto)
    nuevo_producto['_id'] = str(resultado.inserted_id)
    return jsonify(nuevo_producto), 201

# Ruta para actualizar un documento existente
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    producto = coleccion_productos.find_one({'producto_id': producto_id})
    if producto:
        producto['nombre'] = request.json['nombre']
        producto['precio'] = request.json['precio']
        coleccion_productos.replace_one({'producto_id': producto_id}, producto)
        return jsonify(producto_a_json(producto))
    else:
        return not_found(None)

# Ruta para eliminar un documento
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    resultado = coleccion_productos.delete_one({'producto_id': producto_id})
    if resultado.deleted_count > 0:
        return jsonify({'mensaje': 'Producto eliminado correctamente'}), 200
    else:
        return not_found(None)

if __name__ == '__main__':
    app.run(debug=True)

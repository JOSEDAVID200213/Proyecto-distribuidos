from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

uri = "mongodb+srv://jmunoz6:Rpg200213@cluster0.4xkeaks.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

# Verifica si la conexión se estableció correctamente
try:
    client.admin.command('ping')
    print("Conexión a MongoDB Atlas establecida correctamente.")
    db = client.get_database()
except Exception as e:
    print(f"Error al conectar a MongoDB Atlas: {e}")

# Ruta para obtener todos los documentos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    productos = db.productos.find()
    resultado = []
    for producto in productos:
        resultado.append({'nombre': producto['nombre'], 'precio': producto['precio']})
    return jsonify({'productos': resultado})

# Ruta para obtener un documento por su ID
@app.route('/productos/<id>', methods=['GET'])
def obtener_producto_por_id(id):
    producto = db.productos.find_one_or_404({'_id': id})
    return jsonify({'nombre': producto['nombre'], 'precio': producto['precio']})

# Ruta para crear un nuevo documento
@app.route('/productos', methods=['POST'])
def crear_producto():
    nombre = request.json['nombre']
    precio = request.json['precio']
    producto_id = db.productos.insert_one({'nombre': nombre, 'precio': precio}).inserted_id
    nuevo_producto = db.productos.find_one_or_404({'_id': producto_id})
    return jsonify({'mensaje': 'Producto creado correctamente', 'nombre': nuevo_producto['nombre'], 'precio': nuevo_producto['precio']}), 201

# Ruta para actualizar un documento existente
@app.route('/productos/<id>', methods=['PUT'])
def actualizar_producto(id):
    producto = db.productos.find_one_or_404({'_id': id})
    producto['nombre'] = request.json['nombre']
    producto['precio'] = request.json['precio']
    db.productos.replace_one({'_id': id}, producto)
    return jsonify({'mensaje': 'Producto actualizado correctamente', 'nombre': producto['nombre'], 'precio': producto['precio']})

# Ruta para eliminar un documento
@app.route('/productos/<id>', methods=['DELETE'])
def eliminar_producto(id):
    db.productos.find_one_or_404({'_id': id})
    db.productos.delete_one({'_id': id})
    return jsonify({'mensaje': 'Producto eliminado correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True)
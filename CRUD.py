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
    db = client['distribuidos']
    coleccion_productos = db.productos
except Exception as e:
    print(f"Error al conectar a MongoDB Atlas: {e}")

# Ruta para obtener todos los documentos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    productos = coleccion_productos.find()
    resultado = []
    for producto in productos:
        resultado.append({
            'producto_id': producto['producto_id'],
            'nombre': producto['nombre'],
            'precio': producto['precio']
        })
    return jsonify({'productos': resultado})

# Ruta para obtener un documento por su ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto_por_id(producto_id):
    producto = coleccion_productos.find_one({'producto_id': producto_id})
    if producto:
        return jsonify({
            'producto_id': producto['producto_id'],
            'nombre': producto['nombre'],
            'precio': producto['precio']
        })
    else:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

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
        return jsonify({
            'producto_id': producto['producto_id'],
            'nombre': producto['nombre'],
            'precio': producto['precio']
        })
    else:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

# Ruta para eliminar un documento
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    resultado = coleccion_productos.delete_one({'producto_id': producto_id})
    if resultado.deleted_count > 0:
        return jsonify({'mensaje': 'Producto eliminado correctamente'}), 200
    else:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
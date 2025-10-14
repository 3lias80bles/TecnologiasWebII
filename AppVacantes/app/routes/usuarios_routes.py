from flask import Blueprint, request, jsonify
from app.data import usuarios

usuarios_bp = Blueprint('usuarios', __name__)

#Listado Usuarios
@usuarios_bp.route("/",methods = ['GET'])
def obtener_todos():
    return jsonify(usuarios),200

#Crear Usuarios
@usuarios_bp.route("/",methods = ['POST'])
def crear_usuario():
    nuevo = request.get_json()
    if not nuevo.get('nombre_usuario') or not nuevo.get ('password'):
        return jsonify({'error': 'faltan campos obligatorios'}),400
    nuevo["id"] = len(usuarios)+1
    usuarios.append(nuevo)
    return jsonify({'menssaje': 'Usuario creado exitosamente', 'usuario': nuevo}),201

#Correr la aplicacion 
#probar los endpoints en postman
#Buscar un usuario por id
@usuarios_bp.route('/', methods=['GET'])
def obtener_usuario_por_id(usuario_id):
    for usuario in usuarios:
        if usuario.get('id') == usuario_id:
            return jsonify(usuario), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

#Actualizar informacion de usuario
@usuarios_bp.route('/', methods=['PUT'])
def actualizar_usuario(usuario_id):
    datos_actualizados = request.get_json()
    for usuario in usuarios:
        if usuario.get('id') == usuario_id:
            usuario.update(datos_actualizados)
            return jsonify({'mensaje': 'Usuario actualizado', 'usuario': usuario}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404
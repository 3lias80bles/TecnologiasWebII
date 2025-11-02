# En este archivo iran las rutas o EndPoints que tengan que ver con el CRUD de usuarios.

from flask import Blueprint, request, jsonify
from app.services.UsuarioServices import UsuarioService
from flask_jwt_extended import jwt_required, get_jwt_identity

# Se crea el Blueprint
usuarios_bp = Blueprint('usuarios', __name__)

#Listado Usuarios
@usuarios_bp.route("/",methods = ['GET'])
#@jwt_required() # Proteger la ruta con JWT
def obtener_todos():
    usuarios = UsuarioService.obtener_usuarios()

    # Verificar si hay usuarios, si no hay, retornar un mensaje adecuado.
    if not usuarios:
        return jsonify({"message": 'No hay usuarios en la base de datos'}),404

    return usuarios

#Crear Usuarios
@usuarios_bp.route("/crear", methods = ['POST'])
def crear_usuario():
    nuevo = request.get_json() or {}
    
    respuesta = UsuarioService.crear_usuario(
        nombre_usuario = nuevo.get('nombre_usuario'),
        password = nuevo.get('password'),
        rol_id = nuevo.get('rol_id')
    )
    return respuesta

# Buscar un usuario por id
@usuarios_bp.route('/<int:usuario_id>', methods=['GET'])
def obtener_usuario_por_id(usuario_id):
    usuario = UsuarioService.obtener_usuario_por_id(usuario_id)
    return usuario

# Actualizar informacion de un usuario
@usuarios_bp.route('/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    # Obtener los datos actualizados del usuario desde la solicitud
    datos_actualizados = request.get_json() or {}

    # Llamar al servicio para actualizar el usuario
    usuario = UsuarioService.actualizar_usuario(usuario_id, datos_actualizados)

    return usuario

# Eliminar un usuario por su id
@usuarios_bp.route('/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    # Llamar al servicio para eliminar el usuario
    usuario = UsuarioService.eliminar_usuario(usuario_id)
    return usuario
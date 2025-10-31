from flask import Blueprint, jsonify, request
from app.models.UsuariosModel import RolModel
from app.services.RolService import RolService
from app.extensions import db

roles_bp = Blueprint('roles', __name__)

#Obtener todos los roles
@roles_bp.route('/', methods=['GET'])
def obtener_roles():

    # Hacer querys desde instancia
    # query = db.session.query().filter().order_by() sirve para hacer consultas mas complejas
    # roles = RolModel.query.all() # Query en Python con Flask usando sqlalchemy. Esta es otra forma de hacerlo

    roles = RolService.obtener_roles() # Llamada al servicio para obtener roles.
    roles_json = [
        {
            'id': r.id,
            'nombre_rol': r.nombre_rol,
            'usuarios': [u.nombre_usuario for u in r.usuarios]
        }
        for r in roles
    ]

    # Devuelve los datos en formato JSON.
    return jsonify(roles_json), 200

# Crear un nuevo rol
@roles_bp.route('/crear', methods=['POST'])
def crear_rol():
    nuevo = request.get_json() or {}

    respuesta = RolService.crear_rol(
        nombre_rol=nuevo.get('nombre_rol'))
    return respuesta
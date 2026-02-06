from flask import Blueprint, request, jsonify
from app.models.UsuariosModel import UsuariosModel
from app.services.AuthUsuario import AuthUsuario as AuthUsuario
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json() or {}

        if not data:
            return jsonify({"message": "JSON inválido o vacio"}), 400


        # Verifica las credenciales del usuario
        auth_usuario = AuthUsuario.authenticate_user(
            nombre_usuario=data.get('nombre_usuario'),
            password=data.get('password')
        )
        
        if auth_usuario:
            print("Usuario autenticado:", auth_usuario.nombre_usuario)
            nombre_rol = auth_usuario.rol.nombre_rol
            access_token = create_access_token(
                identity=str(auth_usuario.id), 
                # opcional para agregar más información al token o si queremos hacer validaciones en endpoints
                additional_claims={"role": nombre_rol, "id_usuario": str(auth_usuario.id), "nombre_usuario" : auth_usuario.nombre_usuario}
            )
            refresh_token = create_refresh_token(identity=str(auth_usuario.id))

            return jsonify({"message": "Login exitoso", "access_token": access_token, "refresh_token": refresh_token}), 200

        # Si falla autenticación devolver 401 y no intentar usar variables no inicializadas
        return jsonify({"message": "Credenciales inválidas"}), 401
    except Exception as e:
        print("Error en /login:", repr(e))
        return jsonify({"message": "Error interno del servidor"}), 500
    
    
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}

    if not data:
        return jsonify({"message": "JSON inválido o vacio"}), 400

    return jsonify({"message": "Registro existoso"}), 201
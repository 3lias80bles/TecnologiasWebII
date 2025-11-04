from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from app.services.AuthUsuario import AuthUsuario
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

# -----------------------------
#  LOGIN
# -----------------------------
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}

    nombre_usuario = data.get('nombre_usuario')
    password = data.get('password')

    if not nombre_usuario or not password:
        return jsonify({"error": "Faltan credenciales"}), 400

    # Llamar al servicio de autenticación
    resultado = AuthUsuario.authenticateUser(nombre_usuario, password)

    if not resultado or isinstance(resultado, dict) and "error" in resultado:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

    usuario = resultado  # instancia de UsuariosModel
    rol_nombre = usuario.rol.nombre_rol if hasattr(usuario, 'rol') else "Desconocido"

    # Crear tokens
    access_token = create_access_token(
        identity={"username": usuario.nombre_usuario, "role": rol_nombre},
        expires_delta=timedelta(hours=3),
        additional_claims={"role": rol_nombre}
    )
    refresh_token = create_refresh_token(identity={"username": usuario.nombre_usuario})

    return jsonify({
        "mensaje": "Login exitoso",
        "usuario": usuario.nombre_usuario,
        "rol": rol_nombre,
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200


# -----------------------------
#  REGISTRO (opcional)
# -----------------------------
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    # Puedes conectar aquí con UsuarioService.crear_usuario()
    return jsonify({"mensaje": "El registro es exitoso"}), 201

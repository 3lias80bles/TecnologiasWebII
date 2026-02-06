# En este archivo iran las rutas o EndPoints que tengan que ver con el CRUD de vacantes.
from flask import Blueprint, jsonify, request
from app.services.VacanteService import VacantesService
# Importa decoradores y funciones para manejar tokens JWT y la identidad del usuario.
from flask_jwt_extended import jwt_required, get_jwt

# Creación del Blueprint para agrupar rutas de vacantes.
vacantes_bp = Blueprint('vacantes', __name__)

# Endpoint para listar todas las vacantes (acceso público).

@vacantes_bp.route('/', methods=['GET'])
@jwt_required()
def obtener_todas():
    vacantes = VacantesService.obtener_vacantes()

    if not vacantes:
        return jsonify({'mensaje': 'No hay vacantes disponibles'}), 404

    return jsonify(vacantes)

# Endpoint para listar detalles de una vacante por ID. Requiere autenticación.
@vacantes_bp.route('/<int:vacante_id>', methods=['GET'])
@jwt_required()
def obtener_vacante_por_id(vacante_id):
    # Verifica que el usuario sea 'postulante' para acceder a los detalles.
    rol = get_jwt().get('role')

    if rol != 'postulante':
        return jsonify({'error': 'No tienes permisos para ver los detalles de la vacante'}), 403

    vacante = VacantesService.obtener_vacante_por_id(vacante_id)

    if not vacante:
        return jsonify({'mensaje': 'Vacante no encontrada'}), 404

    return jsonify(vacante)


# Endpoint para listar vacantes creadas por el usuario autenticado ('reclutador').
@vacantes_bp.route('/mis_vacantes', methods=['GET'])
@jwt_required()
def obtener_mis_vacantes():
    # Obtiene el ID del creador desde el token JWT.
    usuario_id = get_jwt().get('id_usuario')
    print("ID del usuario desde el token JWT:", usuario_id)
    
    vacantes = VacantesService.obtener_vacantes_por_usuario(usuario_id)

    if not vacantes:
        return jsonify({'mensaje': 'No has creado vacantes'}), 404

    return jsonify(vacantes)

# Endpoint para listar todas las vacantes disponibles. Solo accesible para 'postulante'.
@vacantes_bp.route('/disponibles', methods=['GET'])
@jwt_required()
def obtener_disponibles():
    # Verifica que el rol sea 'postulante'.
    rol = get_jwt().get('role')

    if rol != 'postulante':
        return jsonify({'error': 'No tienes permisos para ver vacantes disponibles'}), 403

    # Llama al servicio pidiendo TODAS las vacantes disponibles.
    vacantes = VacantesService.obtener_vacantes_disponibles(todas=True)

    if not vacantes:
        return jsonify({'mensaje': 'No hay vacantes disponibles'}), 404

    return jsonify(vacantes)

# Endpoint para listar las 3 vacantes disponibles más recientes. Solo accesible para 'postulante'.
@vacantes_bp.route('/disponibles/ultimas', methods=['GET'])
@jwt_required()
def obtener_ultimas_disponibles():
    # Verifica que el rol sea 'postulante'.
    rol = get_jwt().get('role')

    if rol != 'postulante':
        return jsonify({'error': 'No tienes permisos para ver vacantes disponibles'}), 403

    # Llama al servicio pidiendo SOLO las últimas (todas=False).
    vacantes = VacantesService.obtener_vacantes_disponibles(todas=False)

    if not vacantes:
        return jsonify({'mensaje': 'No hay vacantes disponibles'}), 404

    return jsonify(vacantes)

# Endpoint para crear nuevas vacantes. Solo accesible para 'reclutador'.
@vacantes_bp.route('/crear', methods=['POST'])
@jwt_required()
def crear_vacante():
    # Obtiene el rol y el ID del usuario del token.
    rol = get_jwt().get('role')
    creador = get_jwt().get('id_usuario')

    # Verifica que el rol sea 'reclutador'.
    if rol != 'Reclutador':
        return jsonify({'error': 'No tienes permisos para crear vacantes'}), 403

    # Obtiene los datos del cuerpo de la solicitud JSON.
    nueva = request.get_json() or {}
    
    # Llama al servicio para la creación.
    respuesta = VacantesService.crear_vacante(
        nombre_vacante = nueva.get('nombre_vacante'),
        descripcion = nueva.get('descripcion'),
        detalles = nueva.get('detalles'),
        fecha_publicacion = nueva.get('fecha_publicacion'),
        fecha_edicion = nueva.get('fecha_edicion'),
        estado = nueva.get('estado'),
        creador = creador, # Asigna el ID del creador desde el token
        postulador = nueva.get('postulador')
    )
    return respuesta

# Endpoint para asignar una vacante a un postulante. Solo accesible para 'reclutador'.
@vacantes_bp.route('/asignar/<int:vacante_id>', methods=['PUT'])
@jwt_required()
def asignar_vacante(vacante_id):
    # Verifica que el rol sea 'reclutador'.
    rol = get_jwt().get('role')

    if rol != 'reclutador':
        return jsonify({'error': 'No tienes permisos para asignar vacantes'}), 403

    # Obtiene los datos de actualización (incluyendo 'postulador').
    datos_actualizados = request.get_json() or {}

    # Llama al servicio para la asignación.
    vacante = VacantesService.asignar_vacante(vacante_id, datos_actualizados)

    return vacante

# Endpoint para actualizar/editar una vacante. Requiere autenticación.
@vacantes_bp.route('/<int:vacante_id>', methods=['PUT'])
@jwt_required()
def actualizar_vacante(vacante_id):
    # Obtiene los datos actualizados.
    datos_actualizados = request.get_json() or {}

    # Llama al servicio para la actualización.
    vacante = VacantesService.actualizar_vacante(vacante_id, datos_actualizados)

    return vacante
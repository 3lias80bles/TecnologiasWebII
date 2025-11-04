# En este archivo irán las rutas o EndPoints que tengan que ver con el CRUD de vacantes.

from flask import Blueprint, jsonify, request
from app.models.VacantesModel import VacantesModel
from app.extensions import db
from datetime import date

# Se crea el Blueprint
vacantes_bp = Blueprint('vacantes', __name__)

# -----------------------------
#  Obtener todas las vacantes
# -----------------------------
@vacantes_bp.route('/', methods=['GET'])
def obtener_vacantes():
    vacantes = VacantesModel.query.all()
    
    if not vacantes:
        return jsonify({'mensaje': 'No hay vacantes registradas'}), 404
    
    return jsonify([v.to_dict() for v in vacantes]), 200


# -----------------------------
#  Crear una nueva vacante
# -----------------------------
@vacantes_bp.route('/crear', methods=['POST'])
def crear_vacante():
    data = request.get_json() or {}
    
    nombre_vacante = data.get('nombre_vacante')
    descripcion = data.get('descripcion')
    detalles = data.get('detalles')
    creador = data.get('creador')

    if not nombre_vacante or not descripcion:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    nueva_vacante = VacantesModel(
        nombre_vacante=nombre_vacante,
        descripcion=descripcion,
        detalles=detalles,
        creador=creador,
        fecha_publicacion=date.today()
    )

    try:
        db.session.add(nueva_vacante)
        db.session.commit()
        return jsonify({'mensaje': 'Vacante creada exitosamente', 'vacante': nueva_vacante.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al crear la vacante', 'detalle': str(e)}), 500


# -----------------------------
#  Buscar una vacante por ID
# -----------------------------
@vacantes_bp.route('/<int:vacante_id>', methods=['GET'])
def obtener_vacante_por_id(vacante_id):
    vacante = VacantesModel.query.get(vacante_id)
    if not vacante:
        return jsonify({'error': 'Vacante no encontrada'}), 404
    return jsonify(vacante.to_dict()), 200


# -----------------------------
#  Actualizar una vacante
# -----------------------------
@vacantes_bp.route('/<int:vacante_id>', methods=['PUT'])
def actualizar_vacante(vacante_id):
    vacante = VacantesModel.query.get(vacante_id)
    if not vacante:
        return jsonify({'error': 'Vacante no encontrada'}), 404

    data = request.get_json() or {}

    # Sobrescribir atributos si vienen en el body
    if 'nombre_vacante' in data:
        vacante.nombre_vacante = data['nombre_vacante']
    if 'descripcion' in data:
        vacante.descripcion = data['descripcion']
    if 'detalles' in data:
        vacante.detalles = data['detalles']
    if 'estado' in data:
        vacante.estado = data['estado']
    if 'postulador' in data:
        vacante.postulador = data['postulador']
    
    vacante.fecha_edicion = date.today()

    try:
        db.session.commit()
        return jsonify({'mensaje': 'Vacante actualizada exitosamente', 'vacante': vacante.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al actualizar la vacante', 'detalle': str(e)}), 500


# -----------------------------
#  Eliminar una vacante
# -----------------------------
@vacantes_bp.route('/<int:vacante_id>', methods=['DELETE'])
def eliminar_vacante(vacante_id):
    vacante = VacantesModel.query.get(vacante_id)
    if not vacante:
        return jsonify({'error': 'Vacante no encontrada'}), 404

    try:
        db.session.delete(vacante)
        db.session.commit()
        return jsonify({'mensaje': 'Vacante eliminada exitosamente'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al eliminar la vacante', 'detalle': str(e)}), 500

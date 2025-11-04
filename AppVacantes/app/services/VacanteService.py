from app.models.VacantesModel import VacantesModel
from app.extensions import db
from flask import jsonify

class VacanteService:

    @staticmethod
    def crear_vacante(titulo, descripcion, reclutador_id):
        if not titulo or not descripcion:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        nueva_vacante = VacantesModel(
            titulo=titulo,
            descripcion=descripcion,
            reclutador_id=reclutador_id
        )

        try:
            db.session.add(nueva_vacante)
            db.session.commit()
            return jsonify({'mensaje': 'Vacante creada exitosamente', 'vacante': nueva_vacante.to_dict()}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al crear la vacante', 'detalle': str(e)}), 500

    @staticmethod
    def obtener_vacantes():
        vacantes = VacantesModel.query.filter_by(estado='disponible').all()
        return jsonify([v.to_dict() for v in vacantes]), 200

    @staticmethod
    def actualizar_vacante(vacante_id, data):
        vacante = VacantesModel.query.get(vacante_id)
        if not vacante:
            return jsonify({'error': 'Vacante no encontrada'}), 404

        if 'titulo' in data:
            vacante.titulo = data['titulo']
        if 'descripcion' in data:
            vacante.descripcion = data['descripcion']
        if 'estado' in data:
            vacante.estado = data['estado']
        if 'reclutador_id' in data:
            vacante.reclutador_id = data['reclutador_id']

        try:
            db.session.commit()
            return jsonify({'mensaje': 'Vacante actualizada exitosamente', 'vacante': vacante.to_dict()}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al actualizar la vacante', 'detalle': str(e)}), 500

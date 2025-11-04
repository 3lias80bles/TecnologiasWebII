from app.models.VacantesModel import VacantesModel
from flask import jsonify
from app.extensions import db
from datetime import datetime

class VacantesService:
    
    # Obtiene todas las vacantes de la base de datos.
    @staticmethod
    def obtener_vacantes():
        vacantes = VacantesModel.query.all()
        return [v.to_dict() for v in vacantes]
    
    # Lista detalles específicos de una vacante por ID.
    @staticmethod
    def obtener_vacante_por_id(vacante_id):
        vacante = VacantesModel.query.get(vacante_id)

        if not vacante:
            return None

        # Solo muestra nombre, detalles y fechas de publicación/edición.
        detalles = {
            'nombre_vacante': vacante.nombre_vacante,
            'detalles': vacante.detalles,
            'fecha_publicacion': vacante.fecha_publicacion.isoformat() if vacante.fecha_publicacion else None,
            'fecha_edicion': vacante.fecha_edicion.isoformat() if vacante.fecha_edicion else None
        }

        return detalles

    # Obtiene las vacantes creadas por un usuario específico (creador).
    @staticmethod
    def obtener_vacantes_por_usuario(usuario_id):
        vacantes = VacantesModel.query.filter_by(creador=usuario_id).all()
        return [v.to_dict() for v in vacantes]
    
    # Obtiene vacantes disponibles. Si 'todas' es False, limita a las 3 más recientes.
    @staticmethod
    def obtener_vacantes_disponibles(todas):

        if todas:
            # Obtiene todas las vacantes con estado 'disponible'.
            vacantes = VacantesModel.query.filter_by(estado='disponible').all()
            return [v.to_dict() for v in vacantes]
        else:
            # Obtiene las 3 vacantes disponibles más recientes.
            vacantes = VacantesModel.query.filter_by(estado='disponible').order_by(VacantesModel.fecha_publicacion.desc()).limit(3).all()
            return [v.to_dict() for v in vacantes]
    

    # Crea una nueva vacante en la base de datos.
    @staticmethod
    def crear_vacante(nombre_vacante, descripcion, detalles, fecha_publicacion, fecha_edicion, estado, creador, postulador):
        
        # Validación de campos obligatorios.
        if not nombre_vacante or not descripcion:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400
        
        # Verifica si el nombre de la vacante ya existe.
        if VacantesModel.query.filter_by(nombre_vacante=nombre_vacante).first():
            return jsonify({'error': 'El nombre de la vacante ya existe'}), 400
        
        # Crea la nueva vacante.
        nueva_vacante = VacantesModel(
            nombre_vacante=nombre_vacante,
            descripcion=descripcion,
            detalles=detalles,
            fecha_publicacion=fecha_publicacion,
            fecha_edicion=fecha_edicion,
            estado=estado,
            creador=creador,
            postulador=postulador
        )

        try:
            db.session.add(nueva_vacante)
            db.session.commit()
            return jsonify({'mensaje': 'Vacante creada exitosamente', 'vacante': nueva_vacante.to_dict()}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al guardar la vacante en la base de datos', 'detalle': str(e)}), 500

    # Asigna un postulante a una vacante y cambia su estado a 'Ocupada'.
    @staticmethod
    def asignar_vacante(vacante_id, datos_actualizados):
        vacante = VacantesModel.query.get(vacante_id)
        
        if not vacante:
            return jsonify({'error': 'Vacante no encontrada'}), 404
        
        # Actualiza el postulador y el estado.
        if 'postulador' in datos_actualizados:
            vacante.postulador = datos_actualizados['postulador']
            vacante.estado = 'Ocupada'
        
        try:
            db.session.commit()
            return jsonify({'mensaje': 'Vacante asignada exitosamente', 'vacante': vacante.to_dict()}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al asignar la vacante en la base de datos', 'detalle': str(e)}), 500

    # Actualiza los campos de una vacante existente.
    @staticmethod
    def actualizar_vacante(vacante_id, datos_actualizados):
        vacante = VacantesModel.query.get(vacante_id)
        
        if not vacante:
            return jsonify({'error': 'Vacante no encontrada'}), 404
        
        # Actualiza campos si se encuentran en los datos de entrada.
        if 'nombre_vacante' in datos_actualizados:
            vacante.nombre_vacante = datos_actualizados['nombre_vacante']
        if 'descripcion' in datos_actualizados:
            vacante.descripcion = datos_actualizados['descripcion']
        if 'detalles' in datos_actualizados:
            vacante.detalles = datos_actualizados['detalles']
        
        # Actualiza la fecha de edición.
        vacante.fecha_edicion = datetime.utcnow()
        
        try:
            db.session.commit()
            return jsonify({'mensaje': 'Vacante actualizada exitosamente', 'vacante': vacante.to_dict()}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al actualizar la vacante en la base de datos', 'detalle': str(e)}), 500
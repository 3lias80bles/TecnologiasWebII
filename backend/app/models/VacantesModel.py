# En este archivo irán las tablas o modelos que se van a crear en la base de datos.
from app.extensions import db  # Importar la instancia de db
from datetime import date  # Para manejar fechas

class VacantesModel(db.Model):
    __tablename__ = 'vacantes'  # Nombre de la tabla en la base de datos
    
    id = db.Column(db.Integer, primary_key=True)  # Llave primaria
    nombre_vacante = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.Text)
    detalles = db.Column(db.Text)
    fecha_publicacion = db.Column(db.Date, default=date.today)
    fecha_edicion = db.Column(db.Date)
    estado = db.Column(db.String(20), default="Disponible")  # Ej: Disponible / Cerrada / Asignada
    creador = db.Column(db.String(50))     # Reclutador
    postulador = db.Column(db.String(50))  # Postulante asignado

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_vacante': self.nombre_vacante,
            'descripcion': self.descripcion,
            'detalles': self.detalles,
            'fecha_publicacion': str(self.fecha_publicacion),
            'fecha_edicion': str(self.fecha_edicion) if self.fecha_edicion else None,
            'estado': self.estado,
            'creador': self.creador,
            'postulador': self.postulador
        }

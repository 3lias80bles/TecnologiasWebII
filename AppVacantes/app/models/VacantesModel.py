# En este archivo iran las tablas o modelos que se van a crear en la base de datos.
from app.extensions import db  # Importar la instancia de db

class VacantesModel(db.Model):
    __tablename__ = 'vacantes'  # Nombre de la tabla en la base de datos.
    
    id = db.Column (db.Integer, primary_key = True) # Llave primaria.
    nombre_vacante = db.Column (db.String(50), nullable = False, unique = True)
    descripcion = db.Column (db.Text)
    detalles = db.Column(db.Text)
    fecha_publicacion = db.Columb(db.Date)
    fecha_edicion = db.Column(db.Date)
    estado = db.Column(db.String(20), default = "Disponible")
    creador = db.Column(db.String(50))
    postulador = db.Column(db.String(50))
    
    
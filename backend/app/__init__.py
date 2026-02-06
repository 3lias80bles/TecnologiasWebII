from flask import Flask
from dotenv import load_dotenv
from app.routes.usuarios_routes import usuarios_bp
from app.routes.roles_routes import roles_bp
from app.routes.auth_routes import auth_bp as auth_bp
from app.routes.vacantes_routes import vacantes_bp as vacantes_bp

from .extensions import db,jwt

from app.models.UsuariosModel import UsuariosModel


load_dotenv()

from config import Config

#crear nuestra aplicacion, devolver una instancia de la clase Flask con las configuraciones asignadas
def create_app():
    app = Flask(__name__)

    #Cargar una confguración
    app.config.from_object(Config)

    #Inicializar extensiones
    db.init_app(app)
    jwt.init_app(app)

    # Para probar de manera local: crear/actualizar las tablas sólo si la conexión funciona.
    with app.app_context():
        try:
            #db.drop_all()  # Elimina las tablas en la base de datos si existen. Cada que se reinicie la app se borran los datos.
            db.create_all()  # Crea las tablas en la base de datos si no existen.
        except Exception as e:
            # No romper el arranque por errores de conexión (credenciales/DB apagada).
            print('Advertencia: no se pudieron crear/actualizar las tablas:', e)
    
    #Registrar blueprints
    app.register_blueprint(usuarios_bp,url_prefix='/usuarios')
    app.register_blueprint(roles_bp,url_prefix='/roles')
    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(vacantes_bp, url_prefix='/vacantes')

    return app
from flask import Flask
from dotenv import load_dotenv
from app.routes.usuarios_routes import usuarios_bp
from app.routes.roles_routes import roles_bp
from app.routes.auth_routes import AuthUsuario

from .extensions import db,jwt

from app.models.UsuariosModel import UsuarioModel


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

    #cargar una configuracion
    app.config.from_object('config.Config')


    with app.app_context():
        #db.drop_all()
        db.create_all()

    #Registrar blueprints
    app.register_blueprint(usuarios_bp,urlprefix='/usuarios')
    app.register_blueprint(roles_bp,urlprefix='/roles')
    app.register_blueprint(auth_bp,urlprefix='/auth')

    return app
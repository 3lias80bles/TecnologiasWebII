from flask import Flask
from app.routes.usuarios_routes import usuarios_bp
from .extensions import db

#crear nuestra aplicacion, devolver una instancia de la clase Flask con las configuraciones asignadas
def create_app():
    app = Flask(__name__)

    #Inicializar extensiones
    db.init_app(app)

    #cargar una configuracion
    app.config.from_object('config.Config')

    #Registrar blueprints
    app.register_blueprint(usuarios_bp,urlprefix='/usuarios')

    return app
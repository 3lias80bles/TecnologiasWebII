from app import create_app
from app.extensions import db
from sqlalchemy import text
from sqlalchemy.exc import  ObjectNotExecutableError

app = create_app()

def check_db_connection(app):
    with app.app_context():
        try:
            db.session.execute(text('SELECT 1'))
            print("La conexión a la base de datos fue satisfactoria")
        except ObjectNotExecutableError as e:
            print("Error al conectar la Base de datos: ",e)


if __name__ == '__main__':
    check_db_connection(app)
    app.run(port = app.config['PORT'])

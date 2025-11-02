from flask_sqlalchemy import SQLAlchemy#Se importa
from flask_jwt_extended import JWTManager

db = SQLAlchemy()#ya se puede usar sql en nuestro proyecto
jwt = JWTManager ()
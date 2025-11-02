# En este archivo iran las rutas o EndPoints que tengan que ver con el CRUD de vacantes.
from flask import Blueprint, jsonify, request

# Se crea el Blueprint
vacantes_bp = Blueprint('vacantes', __name__)
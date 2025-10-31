from app.models.UsuariosModel import UsuarioModel
from flask import jsonify

class UsuarioService():
    @staticmethod
    def obtenerUsuarios():
        usuarios =UsuarioModel.query.all()
        return usuarios
    
    @staticmethod
    def crearUsuario(nombre_usuario, password):
        if not nombre_usuario or not password:
            return jsonify({'error': 'Faltan datos obligatorios'}),404
        
        if UsuarioModel.query.filter_by(nombre_usuario=nombre_usuario).first():
            return jsonify({'error': 'Nombre de usuario ya existente'})
        
        usuario = UsuarioModel(
            nombre_usuario=nombre_usuario,
            password = password
            
        )

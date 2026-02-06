# Archivo creado con el fin de implementar la logica de negocio para usuarios.
from app.models.UsuariosModel import UsuariosModel
from flask import jsonify
from app.extensions import db

class UsuarioService:

    @staticmethod
    def obtener_usuarios():
        usuarios = UsuariosModel.query.all()
        
        return [u.to_dict() for u in usuarios]
    
    @staticmethod
    def crear_usuario(nombre_usuario, password, rol_id):

        # Validar campos obligatorios
        if not nombre_usuario or not password:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        # Verificar si ya existe un usuario en UsuariosModel
        if UsuariosModel.query.filter_by(nombre_usuario=nombre_usuario).first():
            return jsonify({'error': 'El nombre de usuario ya existe'}), 400
        
        # Crear el nuevo usuario
        nuevo_usuario = UsuariosModel(
            nombre_usuario=nombre_usuario,
            password=password,
            rol_id=rol_id
        )

        # Try except para manejar errores al guardar en la base de datos
        try:
            # Add sirve para agregar el objeto a la sesión actual
            db.session.add(nuevo_usuario)

            # Commit guarda los cambios en la base de datos
            db.session.commit()
            return jsonify({'mensaje': 'Usuario creado exitosamente', 'usuario': nuevo_usuario.to_dict()}), 201
        except Exception as e:
            return jsonify({'error': 'Error al guardar el usuario en la base de datos', 'detalle': str(e)}), 500
    
    # Buscar usuario por id
    @staticmethod
    def obtener_usuario_por_id(usuario_id):
        usuario = UsuariosModel.query.get(usuario_id)
        if not usuario:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        return usuario.to_dict() 
    
    # Actualizar usuario por id
    @staticmethod
    def actualizar_usuario(usuario_id, datos_actualizados):
        # Busca el usuario en la base de datos
        usuario = UsuariosModel.query.get(usuario_id)
        
        # Verificar si el usuario existe
        if not usuario:
            return jsonify({'error': 'Usuario no encontrado'}), 404

        # Actualizar los campos del usuario
        if 'nombre_usuario' in datos_actualizados:
            usuario.nombre_usuario = datos_actualizados['nombre_usuario']
        if 'password' in datos_actualizados:
            usuario.password = datos_actualizados['password']
        if 'rol_id' in datos_actualizados:
            usuario.rol_id = datos_actualizados['rol_id']

        try:
            db.session.commit()
            return jsonify({'mensaje': 'Usuario actualizado exitosamente', 'usuario': usuario.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': 'Error al actualizar el usuario en la base de datos', 'detalle': str(e)}), 500
        
    # Eliminar usuario por id
    @staticmethod
    def eliminar_usuario(usuario_id):
        # Busca el usuario en la base de datos
        usuario = UsuariosModel.query.get(usuario_id)
        
        # Verificar si el usuario existe
        if not usuario:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        try:
            # Sirve para eliminar el objeto de la sesión actual.
            db.session.delete(usuario)
            db.session.commit()
            return jsonify({'mensaje': 'Usuario eliminado exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': 'Error al eliminar el usuario de la base de datos', 'detalle': str(e)}), 500
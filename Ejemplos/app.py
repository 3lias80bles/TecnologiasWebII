from flask import Flask, jsonify 

app = Flask(__name__)

# Datos simulados
usuarios = [
    {"id": 1, "nombre": "Elias"},
    {"id": 2, "nombre": "Juan"},
]

# Ruta principal
@app.route('/')
def home():
    return "Bienvenido a la API de usuarios 👋"

# Ruta para obtener lista de usuarios en formato JSON
@app.route('/usuarios')
def obtener_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)

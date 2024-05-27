from flask import Blueprint, jsonify

# Se crea una instancia de Blueprint
index = Blueprint("index", __name__)
# url_prefix es un argumento opcional que se le puede pasar a Blueprint para que todas las rutas
# que se definan en el Blueprint tengan un prefijo, en este caso, todas las rutas de este Blueprint
# tendrán un prefijo de /civilizations
# Es decir: localhost:3001/civilizations


# Se crea una ruta en la raíz del servidor
@index.route("/", methods=["GET"])
def get_civilizations():
    return jsonify({"civilizations": "Hello, World!"})

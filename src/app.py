from dotenv import load_dotenv

load_dotenv()

from flask import Flask, jsonify
from .routes import civilizations, index
from .models import Base
from .connection import engine, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Se crea una instancia de Flask
app = Flask(__name__)

print(session.connection().connection)
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
migrate = Migrate(
    app,
    session,
    directory="./src/migrations",
)


# RUTAS
# Se registra el Blueprint en la aplicación, es decir, se le dice a la aplicación que utilice las rutas
app.register_blueprint(civilizations)
app.register_blueprint(index)


# Defino una función que se ejecutará antes de que se ejecute la primera petición
# def init_db():
#     print("QUE ONDAAAAA")
#     """ Inicializa la base de datos, la elimina y la vuelve a crear"""
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)


# init_db()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base
import os

# Se crea el objeto engine que se encargará de la conexión a la base de datos que viene
# desde la variable de entorno DATABASE_URL
uri = os.getenv("DATABASE_URL")
engine = create_engine(uri)

Session = sessionmaker(engine)
# Se crea el objeto Session que se encargará de las transacciones con la base de datos
session = Session()
# Se crea una instancia de Session, que es la que se utilizará para realizar las transacciones

print("Conexión con Postgres exitosa")
Base = declarative_base()
# Se crea una instancia de Base que se utilizará para definir los modelos de la base de datos

# Path: src/connection/db.py

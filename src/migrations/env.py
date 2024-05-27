import logging
from logging.config import fileConfig
from alembic import context
from src.connection import (
    engine,
    Base,
)  # Importa el motor directamente desde tu archivo db.py

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")


# Define la función para obtener el motor SQLAlchemy
def get_engine():
    return engine


# Define la función para obtener la URL del motor
def get_engine_url():
    return str(get_engine().url).replace("%", "%%")


def get_metadata():
    Base.metadata.bind = get_engine()
    return Base.metadata


# Configura la URL del motor en la configuración de Alembic
config.set_main_option("sqlalchemy.url", get_engine_url())

# Configura el metadato objetivo para Alembic
target_metadata = get_metadata()


# Define una función para obtener el metadato de la base de datos
def get_metadata():
    return target_metadata


# Define una función para ejecutar migraciones en modo offline
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=get_metadata(), literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


# Define una función para ejecutar migraciones en modo online
def run_migrations_online():
    connectable = get_engine()
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=get_metadata(),
        )
        with context.begin_transaction():
            context.run_migrations()


# Decide si ejecutar las migraciones en modo offline u online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

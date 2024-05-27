from ..connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey

""" 
"egipcios": {
        "id": 1,
        "nombre": "egipcios",
        "origen": "Egipto",
        "ubicacion": "África",
        "año_inicio": -3150,
        "año_fin": 30,
        "imagen": "egipcios.jpg",
        "descripcion corta": "Los egipcios fueron una civilización antigua que se desarrolló en el noreste de África",
        "etnia": "Afroasiática",
        "idioma": "Egipcio antiguo",
        "religion": "Politeísta",
        "politica": "Monarquía",
        "sociedad": "Jerarquizada",
        "poblacion": "Alrededor de 3 millones de habitantes",
        "periodo": "Antigüedad",
        "calificacion": [
            {"name": "tecnologia", "value": 5},
            {"name": "arte", "value": 5},
            {"name": "ciencia", "value": 5},
            {"name": "historia", "value": 5},
            {"name": "matematicas", "value": 5},
            {"name": "arquitectura", "value": 5},
        ],
        "wars": [
            {"name": "Guerras médicas", "year": -499},
            {"name": "Guerras persas", "year": -499},
            {"name": "Guerras civiles", "year": -499},
            {"name": "Guerras romanas", "year": -499},
        ],
        "dioses": [
            {"name": "Ra", "description": "Dios del sol"},
            {"name": "Osiris", "description": "Dios de la muerte"},
            {"name": "Isis", "description": "Diosa de la maternidad"},
            {"name": "Horus", "description": "Dios del cielo"},
            {"name": "Anubis", "description": "Dios de los muertos"},
        ],
        "figuras": [
            {
                "name": "Cleopatra",
                "description": "Reina de Egipto",
                "image": "cleopatra.jpg",
                "year": -69,
            },
            {
                "name": "Tutankamón",
                "description": "Faraón de Egipto",
                "image": "tutankamon.jpg",
                "year": -1332,
            },
            {
                "name": "Ramsés II",
                "description": "Faraón de Egipto",
                "image": "ramses.jpg",
                "year": -1303,
            },
            {
                "name": "Nefertiti",
                "description": "Reina de Egipto",
                "image": "nefertiti.jpg",
                "year": -1370,
            },
            {
                "name": "Akenatón",
                "description": "Faraón de Egipto",
                "image": "akenaton.jpg",
                "year": -1386,
            },
            {
                "name": "Hatshepsut",
                "description": "Reina de Egipto",
                "image": "hatshepsut.jpg",
                "year": -1508,
            },
            {
                "name": "Imhotep",
                "description": "Arquitecto de Egipto",
                "image": "imhotep.jpg",
                "year": -2667,
            },
            {
                "name": "Ankhesenamón",
                "description": "Reina de Egipto",
                "image": "ankhesenamon.jpg",
                "year": -1348,
            },
            {
                "name": "Ptolomeo I",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -367,
            },
            {
                "name": "Ptolomeo II",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -283,
            },
            {
                "name": "Ptolomeo III",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -246,
            },
            {
                "name": "Ptolomeo IV",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -244,
            },
            {
                "name": "Ptolomeo V",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -210,
            },
            {
                "name": "Ptolomeo VI",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -186,
            },
            {
                "name": "Ptolomeo VII",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -145,
            },
            {
                "name": "Ptolomeo VIII",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -182,
            },
            {
                "name": "Ptolomeo IX",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -143,
            },
            {
                "name": "Ptolomeo X",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -118,
            },
            {
                "name": "Ptolomeo XI",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -107,
            },
            {
                "name": "Ptolomeo XII",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -100,
            },
            {
                "name": "Ptolomeo XIII",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -62,
            },
            {
                "name": "Ptolomeo XIV",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -59,
            },
            {
                "name": "Ptolomeo XV",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -47,
            },
            {
                "name": "Ptolomeo XVI",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -44,
            },
            {
                "name": "Ptolomeo XVII",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -36,
            },
            {
                "name": "Ptolomeo XVIII",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -33,
            },
            {
                "name": "Ptolomeo XIX",
                "description": "Faraón de Egipto",
                "image": "ptolomeo.jpg",
                "year": -29,
            },
        ],
        "periodos": [
            {"name": "Imperio Antiguo", "year": -2686},
            {"name": "Imperio Medio", "year": -2055},
            {"name": "Imperio Nuevo", "year": -1550},
            {"name": "Tercer Período Intermedio", "year": -1070},
            {"name": "Bajo Egipto", "year": -664},
            {"name": "Época Ptolemaica", "year": -332},
            {"name": "Época Romana", "year": 30},
        ],
        "descripcion_larga": "Los egipcios fueron una civilización antigua que se desarrolló en el noreste de África, en la región que hoy es Egipto. La civilización egipcia se desarrolló a lo largo de más de 3000 años, desde el año 3150 a.C. hasta el año 30 a.C. La civilización egipcia es conocida por sus grandes monumentos, como las pirámides y las esfinges, así como por su arte, arquitectura, religión y cultura.",
        "publicaciones": [
            {
                "titulo": "El libro de los muertos",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Ebers",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Científico",
            },
            {
                "titulo": "Papiro de Edwin Smith",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Científico",
            },
            {
                "titulo": "Papiro de Turín",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Histórico",
            },
            {
                "titulo": "Papiro de Harris",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Histórico",
            },
            {
                "titulo": "Papiro de Ipuwer",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Histórico",
            },
            {
                "titulo": "Papiro de Ani",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Kahum",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Hunefer",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Nu",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Ankhsheshonq",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Nany",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Nekht",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Nebseni",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Ani",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Nany",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Nekht",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
            {
                "titulo": "Papiro de Nebseni",
                "autor": "Anónimo",
                "año": -1550,
                "genero": "Religioso",
            },
        ],
        "logros": [
            "Construcción de las pirámides",
            "Desarrollo de la escritura jeroglífica",
            "Desarrollo de la astronomía",
            "Desarrollo de la medicina",
            "Desarrollo de la arquitectura",
        ],
    },
 """


# Define el modelo de la tabla civilization
class civilization(Base):
    __tablename__ = "civilization"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    origin = Column(String)
    initYear = Column(Integer)
    endYear = Column(Integer)
    description = Column(String)

    # Relación con la tabla continent
    continent_id = Column(Integer, ForeignKey("continent.id"))

    # Relación con la tabla civilization_achievements
    achievements_civilizations = Column(String)

    # Relación con la tabla image
    images = Column(String)

    def __init__(
        self,
        nombre,
        origen,
        ubicacion,
        año_inicio,
        año_fin,
        imagen,
        descripcion,
        logros,
    ):
        self.nombre = nombre
        self.origen = origen
        self.ubicacion = ubicacion
        self.año_inicio = año_inicio
        self.año_fin = año_fin
        self.imagen = imagen
        self.descripcion = descripcion
        self.logros = logros
        # Se define el constructor de la clase civilization


class Continent(Base):
    __tablename__ = "continent"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    imagen = Column(String)
    descripcion = Column(String)

    # Relación con la tabla civilization
    civilizations = Column(String)

    def __init__(self, nombre, imagen, descripcion):
        self.nombre = nombre
        self.imagen = imagen
        self.descripcion = descripcion
        # Se define el constructor de la clase Continent


class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    url = Column(String)

    # Relación con la tabla civilization
    civilization_id = Column(Integer, ForeignKey("civilization.id"), nullable=True)

    # Relación con la tabla continent
    continent_id = Column(Integer, ForeignKey("continent.id"), nullable=True)

    def __init__(self, nombre, url):
        self.nombre = nombre
        self.url = url
        # Se define el constructor de la clase Image


class civilization_achievement(Base):
    __tablename__ = "civilizationAchievement"

    id = Column(Integer, primary_key=True)
    civilization_id = Column(Integer, ForeignKey("civilization.id"))
    achievement_id = Column(Integer, ForeignKey("achievement.id"))

    def __init__(self, civilization_id, achievement_id):
        self.civilization_id = civilization_id
        self.achievement_id = achievement_id
        # Se define el constructor de la clase civilization_achivements


class achievement(Base):
    __tablename__ = "achievement"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # Relación con la tabla civilization_achievements
    civilization_achievement = Column(String)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        # Se define el constructor de la clase achivements

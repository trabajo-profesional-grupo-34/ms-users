import peewee

from app.utils.db import db
from .rol_model import Rol

class User(peewee.Model):
    email = peewee.CharField()
    nombre = peewee.CharField()
    password = peewee.CharField()
    idRol = peewee.ForeignKeyField(Rol, backref="Rol")

    class Meta:
        database = db
        schema = "taca"
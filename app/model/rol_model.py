import peewee

from app.utils.db import db

class Rol(peewee.Model):
    #idRol = peewee.IntegerField()
    descripcion = peewee.CharField()

    class Meta:
        database = db
        schema = "taca"
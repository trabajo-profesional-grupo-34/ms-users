from app.model.user_model import User
from app.model.rol_model import Rol


from app.utils.db import db

def create_tables():
    with db:
        db.create_tables([Rol, User])

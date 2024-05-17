from fastapi import HTTPException, status

#from passlib.context import CryptContext

from app.model.user_model import User as UserModel
from app.schema import user_schema
from app.service.auth_service import get_password_hash


#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
#def get_password_hash(password):
#    return pwd_context.hash(password)

def create_user(user: user_schema.UserRegister):

    get_user = UserModel.filter(
                                    (UserModel.email == user.email) 
#                                    | (UserModel.nombre == user.nombre)
                                ).first()
    if get_user:
        msg = "Email already registered"
        if get_user.nombre == user.nombre:
            msg = "Name already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        nombre=user.nombre,
        email=user.email,
        idRol = user.idRol,
        password=get_password_hash(user.password)
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        nombre = db_user.nombre,
        email = db_user.email,
        idRol = int(str(db_user.idRol))
    )

def get_rol(mail : str):

    user = UserModel.filter(UserModel.email == mail).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )
        
    return user.idRol_id

def get_nombre(mail : str):

    user = UserModel.filter(UserModel.email == mail).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )
        
    return user.nombre

def get_usuarios():

    users = UserModel.filter(UserModel.email != None)

    list_user = []
    
    for user in users :
        list_user.append(user)
        
    return list_user


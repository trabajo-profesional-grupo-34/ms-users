from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from app.schema import user_schema
from app.service import user_service
from app.service import auth_service
from app.schema.token_schema import Token

from app.utils.db import get_db


router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.post(
    "/create",
    #status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo usuario"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Crea nuevo usuario en al app
    ### Args
    - email: emial@dominio.com
    - username: nombre de usuario
    - password: password para inicio de sesion.

    ### Returns
    - user: informacion del usuario creado
    """
    return user_service.create_user(user)

@router.post(
    "/login",
    tags=["users"],
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Access token de login
    ### Args
    El servicio recibe los siguientes parametros
    - username:  email
    - password:  password

    ### Returns
    - responde access token y token type
    """
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")

@router.get(
    "/get_id/{mail}",
    tags=["users"]
    )
def get_rol_de_usuario(mail : str):
    return user_service.get_rol(mail)

@router.get(
    "/get_nombre/{mail}",
    tags=["users"]
    )
def get_nombre_de_usuario(mail : str):
    return user_service.get_nombre(mail)


@router.get(
    "/usuarios/",
    tags=["users"]
    )
def Get_Lista_de_usuarios():
    """
    El servicio devuelve lista de usuarios
    """
    return user_service.get_usuarios()
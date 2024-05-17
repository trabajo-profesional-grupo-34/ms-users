from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="nombre.apellido@correo.com"
    )
    nombre: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="nombre apellido"
    )
    idRol: int = Field(
        ...,
        example="1"
    )    


class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="strongpass"
    )
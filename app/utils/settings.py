import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    #db_name = os.getenv('DB_NAME')
    #db_user = os.getenv('DB_USER')
    #db_pass = os.getenv('DB_PASS')
    #db_host = os.getenv('DB_HOST')
    #db_port = os.getenv('DB_PORT')

    #secret_key: str = os.getenv('SECRET_KEY')
    #token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

    db_name: str = "dev"
    db_user: str = "postgres"
    db_pass: str = "pass"
    db_host: str = "localhost"
    db_port: str = "5432"

    secret_key: str = "e97965045c7df14cb4d5760371e7325104a8f33ad5d00c0a506d6fb09d0047db"
    token_expire: int = "1440"
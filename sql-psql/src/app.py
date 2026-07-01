from dotenv import dotenv_values
from fastapi import FastAPI
from pydantic import PostgresDsn

config = dotenv_values()

POSTGRES_USER = config["POSTGRES_USER"] or "postgres"
POSTGRES_PASSWORD = config["POSTGRES_PASSWORD"] or "mysecret"
POSTGRES_HOST = config["POSTGRES_HOST"] or "localhost"
POSTGRES_PORT = config["POSTGRES_PORT"] or "5432"
POSTGRES_DB = config["POSTGRES_DB"] or "mydb"

class db_session:
	

app = FastAPI()

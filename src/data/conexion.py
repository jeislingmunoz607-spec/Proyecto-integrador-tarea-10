import mysql.connector
import os
from dotenv import load_dotenv

ruta_env = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(dotenv_path=ruta_env, override=True)


def obtener_conexion():
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return conexion

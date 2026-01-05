import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Engine, event

db = SQLAlchemy()


# Script para mantener la integridad referencial de las claves de sqlite3 en desarrollo
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, _):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

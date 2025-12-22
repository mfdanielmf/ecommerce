from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String
from app.db.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False, unique=True)
    correo = Column(String(120), nullable=False, unique=True)
    contraseña = Column(String, nullable=False)
    rol = Column(String(20), default="usuario")
    fecha_creacion = Column(DateTime, default=datetime.now(timezone.utc))

    def __init__(self, nombre: str, correo: str, contraseña: str):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = generate_password_hash(password=contraseña)

    def comprobar_contraseña(self, contraseña: str) -> bool:
        return check_password_hash(self.contraseña, contraseña)

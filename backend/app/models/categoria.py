from datetime import datetime, timezone
from app.db.db import db
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class Categoria(db.Model):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(500), nullable=False)
    fecha_creacion = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    # Las categorías tienen 0 o N productos
    productos = relationship(
        "Producto", back_populates="categoria", passive_deletes=True)

    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion":  self.descripcion,
            "fecha_creacion": self.fecha_creacion
        }

from datetime import datetime, timezone

from app.db.db import db

from sqlalchemy import DECIMAL, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Producto(db.Model):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(500), nullable=False)
    precio = Column(DECIMAL(precision=10, scale=2), nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    img_url = Column(String(500), nullable=False)
    fecha_creacion = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    # FK
    id_categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    # Un producto solo tiene 1 categoría y es obligatoria
    categoria = relationship(
        "Categoria", back_populates="productos", passive_deletes=True)

    def __init__(self, nombre: str, descripcion: str, precio: float, stock: int, img_url: str, id_categoria: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.img_url = img_url
        self.id_categoria = id_categoria

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'img_url': self.img_url,
            'fecha_creacion': self.fecha_creacion,
            'id_categoria': self.id_categoria
        }

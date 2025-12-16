from datetime import datetime

from app.db.db import db

from sqlalchemy import DECIMAL, Column, DateTime, Integer, String


class Producto(db.Model):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(500), nullable=True)
    precio = Column(DECIMAL(precision=10, scale=2), nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    img_url = Column(String(500), nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)

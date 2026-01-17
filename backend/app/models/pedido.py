from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.db import db


class Pedido(db.Model):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total = Column(Float, nullable=False)
    status = Column(String(50), default="pendiente")
    fecha_creacion = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    # FK
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    # Un pedido tiene 1 usuario
    usuario = relationship(
        "Usuario", back_populates="pedidos", passive_deletes=True)
    productos_pedido = relationship(
        "ProductoPedido", back_populates="pedidos", passive_deletes=True)

    def __init__(self, total: str, id_usuario: int, status: str = "pendiente"):
        self.total = total
        self.status = status
        self.id_usuario = id_usuario

    def to_dict(self):
        return {
            "id": self.id,
            "total": self.total,
            "status": self.status,
            "fecha_creacion": self.fecha_creacion,
            "id_usuario": self.id_usuario,
            "items": [producto_pedido.to_dict() for producto_pedido in self.productos_pedido]
        }

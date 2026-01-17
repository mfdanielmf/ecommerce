from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db.db import db


class ProductoPedido(db.Model):
    __tablename__ = "productos_pedido"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_pedido = Column(ForeignKey("pedidos.id"), nullable=False)
    id_producto = Column(ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)

    productos = relationship(
        "Producto", back_populates="productos_pedido", passive_deletes=True)
    pedidos = relationship(
        "Pedido", back_populates="productos_pedido", passive_deletes=True)

    def to_dict(self):
        return {
            "id": self.id,
            "id_pedido": self.id_pedido,
            "id_producto": self.id_producto,
            "cantidad": self.cantidad,
            "precio": self.precio,
            "producto": self.productos.to_dict()
        }

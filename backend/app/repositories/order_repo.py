from app.db.db import db
from app.models.pedido import Pedido
from app.models.usuario import Usuario


def get_all_orders_user(usuario: Usuario) -> list[Pedido | None]:
    pedidos: list[Pedido | None] = usuario.pedidos

    return pedidos


def insert_order_db(pedido: Pedido) -> Pedido:
    db.session.add(pedido)
    db.session.commit()

    return pedido

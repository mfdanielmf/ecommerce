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


def get_order_by_id(id: int) -> Pedido | None:
    return Pedido.query.get(id)


def update_pedido(pedido: Pedido) -> Pedido:
    db.session.commit()

    return pedido

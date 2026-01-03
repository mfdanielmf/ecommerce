
from app.db.db import db
from app.models.producto import Producto


def get_all_products() -> list[Producto]:
    productos = Producto.query.all()

    return productos


def get_product_by_id(id: int) -> Producto | None:
    producto = Producto.query.get(id)

    return producto


def insert_product(producto: Producto) -> Producto:
    db.session.add(producto)
    db.session.commit()

    return producto


def delete_product(producto: Producto) -> None:
    db.session.delete(producto)
    db.session.commit()


def update_product(producto: Producto) -> Producto:
    db.session.commit()

    return producto

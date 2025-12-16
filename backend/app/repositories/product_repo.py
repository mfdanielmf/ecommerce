
from app.models.producto import Producto


def get_all_products() -> list[Producto]:
    productos = Producto.query.all()

    return productos

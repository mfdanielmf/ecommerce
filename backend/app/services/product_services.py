from app.models.exceptions import ProductoNoEncontradoException
from app.models.producto import Producto
from app.repositories.product_repo import get_all_products, get_product_by_id


def obtener_todos_los_productos() -> list[Producto]:
    productos = get_all_products()

    return productos


def obtener_producto_id(id: int) -> Producto | ProductoNoEncontradoException:
    producto = get_product_by_id(id)

    if not producto:
        raise ProductoNoEncontradoException()

    return producto

from app.models.producto import Producto
from app.repositories.product_repo import get_all_products


def obtener_todos_los_productos() -> list[Producto]:
    productos = get_all_products()

    return productos

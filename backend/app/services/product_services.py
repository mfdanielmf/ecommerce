from app.models.exceptions import CampoProductoIncorrectoException, ProductoNoEncontradoException
from app.models.producto import Producto
from app.repositories.product_repo import get_all_products, get_product_by_id, insert_product


def obtener_todos_los_productos() -> list[Producto]:
    productos = get_all_products()

    return productos


def obtener_producto_id(id: int) -> Producto | ProductoNoEncontradoException:
    producto = get_product_by_id(id)

    if not producto:
        raise ProductoNoEncontradoException()

    return producto


def insertar_producto_base(nombre: str, descripcion: str, precio: float, stock: int, url_img: str) -> Producto | CampoProductoIncorrectoException:
    if len(nombre) > 50 or len(descripcion) > 500 or precio > 99999999.99 or stock < 0 or len(url_img) > 500:
        raise CampoProductoIncorrectoException()

    producto = Producto(nombre=nombre, descripcion=descripcion,
                        precio=precio, stock=stock, img_url=url_img)

    producto_insertado = insert_product(producto)

    return producto_insertado

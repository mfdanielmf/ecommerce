from app.models.categoria import Categoria
from app.models.exceptions import CampoIncorrectoException, ErrorInternoException, ProductoNoEncontradoException, CategoriaNoEncontradaException
from app.models.producto import Producto
from app.repositories.product_repo import get_all_products, get_product_by_id, insert_product, delete_product, update_product
from app.services.category_services import obtener_categoria_por_nombre


def obtener_todos_los_productos() -> list[Producto]:
    productos = get_all_products()

    return productos


def obtener_producto_id(id: int) -> Producto | ProductoNoEncontradoException:
    producto = get_product_by_id(id)

    if not producto:
        raise ProductoNoEncontradoException()

    return producto


def insertar_producto_base(data) -> Producto | CampoIncorrectoException | ErrorInternoException | CategoriaNoEncontradaException:
    try:
        nombre: str = data["nombre"]
        descripcion: str = data["descripcion"]
        stock: int = int(data["stock"])
        precio: float = float(data["precio"])
        url_img: str = data["url"]
        nombre_categoria: str = data["categoria"]

        if len(nombre) < 1 or len(nombre) > 50 or len(descripcion) < 1 or len(descripcion) > 500 or precio < 0 or precio > 99999999.99 or stock < 0 or len(url_img) < 1 or len(url_img) > 500:
            raise CampoIncorrectoException()

        categoria = obtener_categoria_por_nombre(nombre_categoria)

        producto = Producto(nombre=nombre, descripcion=descripcion,
                            precio=precio, stock=stock, img_url=url_img, id_categoria=categoria.id)

        producto_insertado = insert_product(producto)

        return producto_insertado
    except ValueError:
        raise ErrorInternoException()
    except CategoriaNoEncontradaException:
        raise CategoriaNoEncontradaException()


def eliminar_producto_base(id: int) -> None | ProductoNoEncontradoException:
    try:
        producto = obtener_producto_id(id)

        delete_product(producto)
    except ProductoNoEncontradoException:
        raise ProductoNoEncontradoException()


def actualizar_datos_producto(id: int, data) -> Producto | ProductoNoEncontradoException | CampoIncorrectoException | ErrorInternoException:
    try:
        producto: Producto = obtener_producto_id(id)

        nombre: str = data["nombre"]
        descripcion: str = data["descripcion"]
        precio: float = float(data["precio"])
        stock: int = int(data["stock"])
        img_url: str = data["url"]
        nombre_categoria: str = data["categoria"]

        if len(nombre) < 1 or len(nombre) > 50 or len(descripcion) < 1 or len(descripcion) > 500 or precio < 0 or precio > 99999999.99 or stock < 0 or len(img_url) < 1 or len(img_url) > 500:
            raise CampoIncorrectoException()

        try:
            categoria: Categoria = obtener_categoria_por_nombre(
                nombre_categoria)

            # Actualizamos los datos del producto y llamamos al repo para que haga commit de los cambios
            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.precio = precio
            producto.stock = stock
            producto.img_url = img_url
            producto.id_categoria = categoria.id
        except CategoriaNoEncontradaException:
            raise CampoIncorrectoException()

        producto_actualizado: Producto = update_product(producto)

        return producto_actualizado

    except ProductoNoEncontradoException:
        raise ProductoNoEncontradoException()
    except ValueError:
        raise ErrorInternoException()

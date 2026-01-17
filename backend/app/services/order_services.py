from typing import Any
from app.models.exceptions import CampoIncorrectoException, NoHayPedidosException, NoHayProductosException, ProductoNoEncontradoException, UsuarioNoExistenteException
from app.models.pedido import Pedido
from app.models.producto import Producto
from app.models.usuario import Usuario
from app.repositories.order_repo import get_all_orders_user
from app.services.user_services import buscar_usuario_id
from app.services.product_services import obtener_producto_id


def insertar_pedido_base(data) -> CampoIncorrectoException | ProductoNoEncontradoException:
    productos: list[Producto] = validar_producto_order(data)

    pass


def validar_producto_order(data) -> list[Producto] | CampoIncorrectoException | ProductoNoEncontradoException:
    if not data or not data.get("carrito"):
        raise NoHayProductosException()

    productos_validados: list[Producto] = []

    for producto in data["carrito"]:
        if not producto.get("id") or not producto.get("nombre") or not producto.get("precio") or not producto.get("cantidad") or not producto.get("img_url") or producto.get("stock") is None or producto.get("stock") < 1:
            raise CampoIncorrectoException()

        try:
            id: int = int(producto["id"])
            stock: int = int(producto["stock"])
            precio: float = float(producto["precio"])

            producto_base: Producto = obtener_producto_id(id)

            if producto_base.stock < stock or producto_base.precio != precio:
                raise CampoIncorrectoException()

            productos_validados.append(producto_base)
        except ValueError:
            raise CampoIncorrectoException()

    return productos_validados


def obtener_todos_pedidos_usuario(id_usuario: int) -> Any | UsuarioNoExistenteException | NoHayPedidosException:
    usuario: Usuario = buscar_usuario_id(id_usuario)

    if usuario:
        pedidos_database: list[Pedido | None] = get_all_orders_user(usuario)

    # Si no tiene pedidos, salimos
    if len(pedidos_database) < 1:
        raise NoHayPedidosException()

    pedidos: list[dict[Any]] = []

    for pedido in pedidos_database:
        pedidos.append(pedido.to_dict())

    return pedidos

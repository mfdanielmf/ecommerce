from typing import Any
from app.models.exceptions import CampoIncorrectoException, NoHayPedidosException, NoHayProductosException, ProductoNoEncontradoException, UsuarioNoExistenteException
from app.models.pedido import Pedido
from app.models.producto import Producto
from app.models.producto_pedido import ProductoPedido
from app.models.usuario import Usuario
from app.repositories.order_repo import get_all_orders_user, insert_order_db
from app.services.user_services import buscar_usuario_id
from app.services.product_services import obtener_producto_id

# CUANDO ACABE TODO PASAR ID DE USUARIO REAL (DEL TOKEN JWT) DE MOMENTO ASÍ PARA TESTEAR !!!!!!!


def insertar_pedido_base(data) -> None:
    items, total = validar_productos_order(data)

    pedido: Pedido = Pedido(total=total, id_usuario=5)

    for item in items:
        producto_pedido = ProductoPedido(
            producto=item["producto"], cantidad=item["cantidad"])
        pedido.productos_pedido.append(producto_pedido)

    pedido = insert_order_db(pedido)

    return pedido


def validar_productos_order(data) -> tuple[list[dict[Producto, int]], float] | NoHayProductosException | CampoIncorrectoException | ProductoNoEncontradoException:
    if not data or not data.get("carrito"):
        raise NoHayProductosException()

    productos_validados: list[dict[Producto, int]] = []
    total: float = 0

    for producto in data["carrito"]:
        if not producto.get("id") or not producto.get("precio") or producto.get("cantidad") is None or producto.get("cantidad") < 1:
            raise CampoIncorrectoException()

        try:
            id: int = int(producto["id"])
            cantidad: int = int(producto["cantidad"])
            precio: float = float(producto["precio"])

            producto_base: Producto = obtener_producto_id(id)

            if producto_base.stock < cantidad or float(producto_base.precio) != precio:
                raise CampoIncorrectoException()

            total += cantidad * precio

            productos_validados.append(
                {"producto": producto_base, "cantidad": cantidad})
        except ValueError:
            raise CampoIncorrectoException()
        except ProductoNoEncontradoException:
            raise ProductoNoEncontradoException(
                f"No se ha encontrado el producto con id {id}")

    return productos_validados, total


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

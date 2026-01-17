from typing import Any
from app.models.exceptions import NoHayPedidosException, UsuarioNoExistenteException
from app.models.pedido import Pedido
from app.models.producto import Producto
from app.models.usuario import Usuario
from app.repositories.order_repo import get_all_orders_user
from app.services.user_services import buscar_usuario_id


def obtener_todos_pedidos_usuario(id_usuario: int) -> Any | UsuarioNoExistenteException | NoHayPedidosException:
    usuario: Usuario = buscar_usuario_id(id_usuario)

    if usuario:
        pedidos_database: list[Pedido | None] = get_all_orders_user(usuario)

    # Si no tiene pedidos, salimos
    if len(pedidos_database) < 1:
        raise NoHayPedidosException()

    pedidos: list[dict[Pedido]] = []
    productos_pedidos: list[dict[Producto]] = []

    for pedido in pedidos_database:
        for producto_pedido in pedido.productos_pedido:
            cantidad: int = producto_pedido.cantidad
            precio: float = producto_pedido.precio
            producto: Producto = producto_pedido.productos

            productos_pedidos.append(
                {"cantidad": cantidad, "precio": precio, "producto": producto.to_dict()})

        pedidos.append({**pedido.to_dict(), "productos": productos_pedidos})

    return pedidos

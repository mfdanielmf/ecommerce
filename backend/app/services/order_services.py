from typing import Any
from app.models.exceptions import CampoIncorrectoException, EstadoIncorrectoException, NoHayPedidosException, NoHayProductosException, PedidoNoEncontradoException, ProductoNoEncontradoException, StockInsuficienteException, UsuarioNoExistenteException
from app.models.pedido import Pedido
from app.models.producto import Producto
from app.models.producto_pedido import ProductoPedido
from app.models.usuario import Usuario
from app.repositories.order_repo import get_all_orders_user, insert_order_db, get_order_by_id, update_pedido
from app.services.user_services import buscar_usuario_id
from app.services.product_services import obtener_producto_id

# CUANDO ACABE TODO PASAR ID DE USUARIO REAL (DEL TOKEN JWT) DE MOMENTO ASÍ PARA TESTEAR !!!!!!!


def obtener_pedido_por_id(id: int) -> Pedido | PedidoNoEncontradoException:
    pedido: Pedido | None = get_order_by_id(id)

    if not pedido:
        raise PedidoNoEncontradoException()

    return pedido


def insertar_pedido_base(data, id_usuario) -> Pedido | NoHayProductosException | CampoIncorrectoException | ProductoNoEncontradoException:
    # Raises NoHayProductosException | CampoIncorrectoException | ProductoNoEncontradoException
    items, total = validar_productos_order(data)

    pedido: Pedido = Pedido(total=total, id_usuario=id_usuario)

    for item in items:
        producto: Producto = item["producto"]
        cantidad: int = item["cantidad"]

        producto_pedido = ProductoPedido(
            producto=producto, cantidad=cantidad)
        pedido.productos_pedido.append(producto_pedido)

        # Restamos el stock al hacer el pedido del producto (ya hacemos commit de todo cuando se inserta el pedido)
        producto.stock -= cantidad

    pedido = insert_order_db(pedido)

    return pedido


def validar_productos_order(data) -> tuple[list[dict[Producto, int]], float] | NoHayProductosException | CampoIncorrectoException | ProductoNoEncontradoException:
    if not data or not data.get("carrito"):
        raise NoHayProductosException()

    productos_validados: list[dict[Producto, int]] = []
    total: float = 0

    for producto in data["carrito"]:
        if not producto.get("id") or producto.get("precio") is None or producto.get("cantidad") is None or producto.get("cantidad") < 1:
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


def actualizar_pedido(id: int, estado: str) -> Pedido | PedidoNoEncontradoException | EstadoIncorrectoException | ProductoNoEncontradoException | StockInsuficienteException:
    estados: list[str] = ["pendiente", "reparto", "entregado", "cancelado"]

    if not estado in estados:
        raise EstadoIncorrectoException(
            f"Estado incorrecto. Estados disponibles: {[estado for estado in estados]}")

    # Raises PedidoNoEncontradoException
    pedido: Pedido = obtener_pedido_por_id(id)

    # Si ya está cancelado, no lo hacemos (para evitar subir el stock)
    if pedido.status == "cancelado" and estado == "cancelado":
        raise EstadoIncorrectoException(
            f"El pedido con id {pedido.id} ya está cancelado")

    #  Si ya estaba cancelado y lo quiere volvera a abrir, volvemos a restar el stock y si no es posible raise
    if pedido.status == "cancelado" and estado != "cancelado":
        # Raises ProductoNoEnontradoException | StockInsuficienteException
        ajustar_stock(pedido=pedido, sumar=False)

    if estado == "cancelado":
        # Raises ProductoNoEnontradoException
        ajustar_stock(pedido=pedido, sumar=True)

    pedido.status = estado
    pedido_actualizado: Pedido = update_pedido(pedido)

    return pedido_actualizado


def ajustar_stock(pedido: Pedido, sumar: bool) -> None | ProductoNoEncontradoException | StockInsuficienteException:
    for producto_pedido in pedido.productos_pedido:
        id_producto: int = producto_pedido.id_producto
        cantidad: int = producto_pedido.cantidad

        # Raises ProductoNoencontradoException
        # Ya hacemos commit de los cambios en la función que lo llama
        try:
            producto: Producto = obtener_producto_id(id_producto)

            if sumar:
                producto.stock += cantidad
            elif (producto.stock - cantidad) < 0:
                raise StockInsuficienteException(
                    f"No se puede reabrir el pedido. Stock insuficiente para {producto.nombre}. Actual: {producto.stock} Pedido: {cantidad}")
            else:
                producto.stock -= cantidad
        except ProductoNoEncontradoException:
            raise ProductoNoEncontradoException(
                f"No se ha encontrado el producto con id {id_producto}")

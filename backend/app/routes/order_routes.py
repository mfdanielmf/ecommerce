from flask import Blueprint, jsonify

from app.models.pedido import Pedido

from app.services.order_services import obtener_todos_pedidos_usuario

pedido_bp = Blueprint("pedidos", __name__)


# GET TODOS
@pedido_bp.route("/<int:id>")
def get_pedidos_usuario(id: int):
    """
    Voy a devolver los datos asi:
    msg: "Pedidos obtenidos correctamente"
    pedido:
        id, total, status, fecha
        productos:
            id, nombre, descripcion, precio, stock, img_url, id categoria
    """
    data = obtener_todos_pedidos_usuario(id)

    return jsonify({
        "msg": "Pedidos cargados con éxito",
        "pedidos": data
    }), 200

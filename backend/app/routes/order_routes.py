from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.exceptions import CampoIncorrectoException, NoHayPedidosException, NoHayProductosException, PedidoNoEncontradoException, ProductoNoEncontradoException, StockInsuficienteException, UsuarioNoExistenteException, EstadoIncorrectoException
from app.models.pedido import Pedido
from app.repositories.order_repo import update_pedido
from app.services.order_services import insertar_pedido_base, obtener_todos_pedidos_usuario, actualizar_pedido, obtener_pedido_por_id

pedido_bp = Blueprint("pedidos", __name__)

# ------------- AÑADIR JWT A EDITAR PEDIDOS CUANDO HAGAMOS EL PANEL DE PEDIDOS ADMIN --------------------


# GET PEDIDOS USUARIO
@pedido_bp.route("/")
@jwt_required()
def get_pedidos_usuario():
    id: int = int(get_jwt_identity())

    try:
        data = obtener_todos_pedidos_usuario(id)

        return jsonify({
            "msg": "Pedidos cargados con éxito",
            "pedidos": data
        }), 200
    except UsuarioNoExistenteException:
        return jsonify({"error": f"No se ha encontrado el usuario con id {id}"}), 404
    except NoHayPedidosException:
        return jsonify({
            "msg": "Pedidos cargados con éxito",
            "pedidos": []
        }), 200


# INSERTAR PEDIDO
@pedido_bp.route("", methods=["POST"])
@jwt_required()
def post_pedido():
    id_usuario: int = int(get_jwt_identity())

    data = request.get_json()

    try:
        pedido: Pedido = insertar_pedido_base(data=data, id_usuario=id_usuario)

        return jsonify({
            "msg": "¡Pedido realizado correctamente!",
            "pedido": pedido.to_dict()
        }), 200
    except NoHayProductosException:
        return jsonify({"error": "No has pedido ningún objeto"}), 400
    except CampoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422
    except ProductoNoEncontradoException as e:
        return jsonify({"error": str(e)}), 404


# EDITAR ESTADO PEDIDO
@pedido_bp.route("/<int:id>", methods=["PUT"])
def put_pedido(id: int):
    data = request.get_json()

    if not data or not data.get("estado"):
        return jsonify({"error": "No has introducido el nuevo estado del pedido"}), 400

    try:
        pedido: Pedido = actualizar_pedido(id, data["estado"])

        return jsonify({
            "msg": "Se ha actualizado el estado del pedido correctamente",
            "pedido": pedido.to_dict()
        }), 200

    except PedidoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el pedido con id {id}"}), 404
    except EstadoIncorrectoException as e:
        return jsonify({"error": str(e)}), 400
    except ProductoNoEncontradoException as e2:
        return jsonify({"error": str(e2)}), 404
    except StockInsuficienteException as e3:
        return jsonify({"error": str(e3)}), 500


# CANCELAR PEDIDO
@pedido_bp.route("/<int:id_pedido>/cancelar", methods=["PUT"])
@jwt_required()
def cancelar_pedido(id_pedido):
    id_usuario: int = int(get_jwt_identity())

    try:
        pedido: Pedido = obtener_pedido_por_id(id_pedido)

        if (pedido.usuario.id != id_usuario):
            return jsonify({"error": "No tienes acceso a este pedido"})

        pedido.status = "cancelado"

        pedido_actualizado: Pedido = update_pedido(pedido=pedido)

        return jsonify({
            "msg": "Se ha cancelado el pedido correctamente",
            "pedido": pedido_actualizado.to_dict()
        })
    except PedidoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el pedido con id {id_pedido}"}), 404

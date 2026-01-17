from flask import Blueprint, jsonify, request

from app.models.exceptions import CampoIncorrectoException, NoHayPedidosException, NoHayProductosException, ProductoNoEncontradoException, UsuarioNoExistenteException
from app.models.pedido import Pedido
from app.services.order_services import insertar_pedido_base, obtener_todos_pedidos_usuario

pedido_bp = Blueprint("pedidos", __name__)


# GET PEDIDOS USUARIO
@pedido_bp.route("/<int:id>")
def get_pedidos_usuario(id: int):
    # RECIBIR ID POR TOKEN JWT CUANDO LO TENGAMOS TODO TESTEADO Y ACABADO !!!!!!!!!!!!!
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
@pedido_bp.route("/", methods=["POST"])
def post_pedido():
    data = request.get_json()

    try:
        pedido: Pedido = insertar_pedido_base(data)

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

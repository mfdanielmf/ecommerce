from flask import Blueprint, jsonify, request

from app.services.order_services import obtener_todos_pedidos_usuario

pedido_bp = Blueprint("pedidos", __name__)


# GET PEDIDOS USUARIO
@pedido_bp.route("/<int:id>")
def get_pedidos_usuario(id: int):
    # RECIBIR ID POR TOKEN JWT CUANDO LO TENGAMOS TODO TESTEADO Y ACABADO !!!!!!!!!!!!!
    data = obtener_todos_pedidos_usuario(id)

    return jsonify({
        "msg": "Pedidos cargados con éxito",
        "pedidos": data
    }), 200


# INSERTAR PEDIDO
@pedido_bp.route("/", methods=["POST"])
def post_pedido():
    data = request.get_json()

    if not data or not data.get("id") or not data.get("nombre") or not data.get("precio") or not data.get("cantidad") or not data.get("img_url") or not data.get("stock"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    pass

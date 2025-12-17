from flask import Blueprint, jsonify
from flask_cors import cross_origin

from app.models.exceptions import ProductoNoEncontradoException
from app.models.producto import Producto
from app.services.product_services import obtener_todos_los_productos, obtener_producto_id

producto_bp = Blueprint("productos", __name__)


@producto_bp.route("/")
@cross_origin()
def productos():
    productos: list[Producto] = obtener_todos_los_productos()

    return jsonify({"products": [producto.to_dict() for producto in productos]}), 200


@producto_bp.route("/<int:id>")
@cross_origin()
def producto_id(id):
    try:
        producto = obtener_producto_id(id)

        return jsonify({"producto": producto.to_dict()}), 200
    except ProductoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el producto con id {id}"}), 404

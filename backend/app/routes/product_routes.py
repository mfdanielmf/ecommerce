from flask import Blueprint, jsonify
from flask_cors import cross_origin

from app.models.producto import Producto
from app.services.product_services import obtener_todos_los_productos

producto_bp = Blueprint("productos", __name__)


@producto_bp.route("/")
@cross_origin()
def productos():
    productos: list[Producto] = obtener_todos_los_productos()

    return jsonify({"products": [producto.to_dict() for producto in productos]}), 200

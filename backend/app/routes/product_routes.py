from flask import Blueprint, jsonify, request

from app.models.exceptions import ProductoNoEncontradoException, CampoProductoIncorrectoException
from app.models.producto import Producto
from app.services.product_services import obtener_todos_los_productos, obtener_producto_id, insertar_producto_base

producto_bp = Blueprint("productos", __name__)


@producto_bp.route("/")
def productos():
    productos: list[Producto] = obtener_todos_los_productos()

    return jsonify({"products": [producto.to_dict() for producto in productos]}), 200


@producto_bp.route("/<int:id>")
def producto_id(id):
    try:
        producto = obtener_producto_id(id)

        return jsonify({"producto": producto.to_dict()}), 200
    except ProductoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el producto con id {id}"}), 404


@producto_bp.route("/insertar", methods=["POST"])
def insertar_producto():
    data = request.get_json()

    print(data)

    if not data or not data.get("nombre") or not data.get("descripcion") or (data.get("stock") is None) or (data.get("precio") is None) or not data.get("url"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    nombre: str = data["nombre"]
    descripcion: str = data["descripcion"]
    stock: int = data["stock"]
    precio: float = data["precio"]
    url: str = data["url"]

    try:
        producto = insertar_producto_base(
            nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, url_img=url)

        return jsonify({
            "msg": "Producto añadido correctamente",
            "producto": producto.to_dict()
        }), 200
    except CampoProductoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422

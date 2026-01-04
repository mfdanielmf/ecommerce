from flask import Blueprint, jsonify, request

from app.models.exceptions import ErrorInternoException, ProductoNoEncontradoException, CampoProductoIncorrectoException
from app.models.producto import Producto
from app.services.product_services import obtener_todos_los_productos, obtener_producto_id, insertar_producto_base, eliminar_producto_base, actualizar_datos_producto

producto_bp = Blueprint("productos", __name__)


# GET TODOS
@producto_bp.route("/")
def get_productos():
    productos: list[Producto] = obtener_todos_los_productos()

    return jsonify({"products": [producto.to_dict() for producto in productos]}), 200


# GET PRODUCTO POR ID
@producto_bp.route("/<int:id>")
def get_producto_id(id):
    try:
        producto = obtener_producto_id(id)

        return jsonify({"producto": producto.to_dict()}), 200
    except ProductoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el producto con id {id}"}), 404


# POST INSERTAR PRODUCTO
@producto_bp.route("/", methods=["POST"])
def post_insertar_producto():
    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("descripcion") or (data.get("stock") is None) or (data.get("precio") is None) or not data.get("url"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        producto = insertar_producto_base(data)

        return jsonify({
            "msg": "Producto añadido correctamente",
            "producto": producto.to_dict()
        }), 200
    except CampoProductoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422
    except ErrorInternoException:
        return jsonify({"error": "Ha ocurrido un error en la petición"}), 500


# DELETE ELIMINAR PRODUCTO
@producto_bp.route("/<int:id>", methods=["DELETE"])
def delete_producto(id):
    try:
        eliminar_producto_base(id)

        return jsonify({"msg": "Producto eliminado correctamente"}), 200

    except ProductoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el producto con id {id}"}), 404


# ACTUALIZAR PRODUCTO
@producto_bp.route("/<int:id>", methods=["PUT"])
def actualizar_producto(id):
    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("descripcion") or (data.get("stock") is None) or (data.get("precio") is None) or not data.get("url"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        producto = actualizar_datos_producto(id, data)

        return jsonify({
            "msg": "El producto se ha actualizado correctamente",
            "producto": producto.to_dict()
        }), 200

    except ProductoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el producto con id {id}"}), 404
    except CampoProductoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422
    except ErrorInternoException:
        return jsonify({"error": "Ha ocurrido un error en la petición"}), 500

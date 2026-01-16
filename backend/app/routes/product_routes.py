from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt

from app.models.exceptions import ErrorInternoException, ProductoNoEncontradoException, CampoIncorrectoException
from app.models.producto import Producto
from app.services.product_services import obtener_todos_los_productos, obtener_producto_id, insertar_producto_base, eliminar_producto_base, actualizar_datos_producto
from app.services.user_services import comprobar_usuario_es_admin

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
@jwt_required()
def post_insertar_producto():
    data = get_jwt()

    if comprobar_usuario_es_admin(data) is False:
        return jsonify({"error": "Acción cancelada. El usuario no es admin"}), 403

    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("descripcion") or (data.get("stock") is None) or (data.get("precio") is None) or not data.get("url") or not data.get("categoria"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        producto = insertar_producto_base(data)

        return jsonify({
            "msg": "Producto añadido correctamente",
            "producto": producto.to_dict()
        }), 200
    except CampoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422
    except ErrorInternoException:
        return jsonify({"error": "Ha ocurrido un error en la petición"}), 500


# DELETE ELIMINAR PRODUCTO
@producto_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_producto(id):
    data = get_jwt()

    if comprobar_usuario_es_admin(data) is False:
        return jsonify({"error": "Acción cancelada. El usuario no es admin"}), 403

    try:
        producto_eliminado: Producto = eliminar_producto_base(id)

        return jsonify({
            "msg": "Producto eliminado correctamente",
            "producto": producto_eliminado
        }), 200

    except ProductoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el producto con id {id}"}), 404


# ACTUALIZAR PRODUCTO
@producto_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def actualizar_producto(id):
    data = get_jwt()

    if comprobar_usuario_es_admin(data) is False:
        return jsonify({"error": "Acción cancelada. El usuario no es admin"}), 403

    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("descripcion") or (data.get("stock") is None) or (data.get("precio") is None) or not data.get("url") or not data.get("categoria"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        producto = actualizar_datos_producto(id, data)

        return jsonify({
            "msg": "El producto se ha actualizado correctamente",
            "producto": producto.to_dict()
        }), 200

    except ProductoNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el producto con id {id}"}), 404
    except CampoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422
    except ErrorInternoException:
        return jsonify({"error": "Ha ocurrido un error en la petición"}), 500

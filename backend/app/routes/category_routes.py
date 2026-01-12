from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt, jwt_required

from app.models.exceptions import CampoIncorrectoException, CategoriaConProductosException, CategoriaYaExistenteException, CategoriaNoEncontradaException
from app.services.category_services import obtener_todas_categorias, insertar_categoria_base, eliminar_categoria_base, actualizar_categoria
from app.services.auth_services import comprobar_usuario_es_admin

from app.models.categoria import Categoria

categoria_bp = Blueprint("categorias", __name__)


# GET TODAS LAS CATEGORÍAS
@categoria_bp.route("/")
def get_categorias():
    categorias: list[Categoria] = obtener_todas_categorias()

    return jsonify({"categorias": [categoria.to_dict() for categoria in categorias]}), 200


# POST INSERTAR CATEGORÍA
@categoria_bp.route("/", methods=["POST"])
@jwt_required()
def post_categoria():
    data = get_jwt()

    if comprobar_usuario_es_admin(data) is False:
        return jsonify({"error": "Acción cancelada. El usuario no es admin"}), 403

    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("descripcion"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        categoria: Categoria = insertar_categoria_base(data)

        return jsonify({
            "msg": "Categoría creada correctamente",
            "categoria": categoria.to_dict()
        }), 200
    except CategoriaYaExistenteException:
        return jsonify({"error": f"Ya existe una categoría con el nombre {data["nombre"]}"}), 409
    except CampoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422


# DELETE CATEGORÍA
@categoria_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def del_categoria(id):
    data = get_jwt()

    if comprobar_usuario_es_admin(data) is False:
        return jsonify({"error": "Acción cancelada. El usuario no es admin"}), 403

    try:
        eliminar_categoria_base(id)

        return jsonify({"msg": "Categoría eliminada correctamente"}), 200
    except CategoriaNoEncontradaException:
        return jsonify({"error": f"No se ha encontrado la categoría con id {id}"}), 404
    except CategoriaConProductosException:
        return jsonify({"error": "La categoría tiene productos. Elimínalos para continuar"}), 409


# EDITAR CATEGORÍA
@categoria_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def put_categoria(id):
    data = get_jwt()

    if comprobar_usuario_es_admin(data) is False:
        return jsonify({"error": "Acción cancelada. El usuario no es admin"}), 403

    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("descripcion"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        categoria: Categoria = actualizar_categoria(data, id)

        return jsonify({
            "msg": "La categoría se ha actualizado correctamente",
            "categoria": categoria.to_dict()
        }), 200
    except CampoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422
    except CategoriaNoEncontradaException:
        return jsonify({"error": f"No se ha encontrado la categoría con id {id}"}), 404
    except CategoriaYaExistenteException:
        return jsonify({"error": f"Ya existe una categoría con nombre {data['nombre']}"}), 409

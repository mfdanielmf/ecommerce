from flask import Blueprint, jsonify, request

from app.models.exceptions import CampoIncorrectoException, CategoriaYaExistenteException
from app.services.category_services import obtener_todas_categorias, insertar_categoria_base

from app.models.categoria import Categoria

categoria_bp = Blueprint("categorias", __name__)


# GET TODAS LAS CATEGORÍAS
@categoria_bp.route("/")
def get_categorias():
    categorias: list[Categoria] = obtener_todas_categorias()

    return jsonify({"categorias": [categoria.to_dict() for categoria in categorias]}), 200


# POST INSERTAR CATEGORÍA
@categoria_bp.route("/", methods=["POST"])
def post_categoria():
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

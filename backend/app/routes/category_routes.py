from flask import Blueprint, jsonify

from app.services.category_services import obtener_todas_categorias

from app.models.categoria import Categoria

categoria_bp = Blueprint("categorias", __name__)


@categoria_bp.route("/")
def get_categorias():
    categorias: list[Categoria] = obtener_todas_categorias()

    return jsonify({"categorias": [categoria.to_dict() for categoria in categorias]}), 200

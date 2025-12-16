from flask import Blueprint, jsonify

producto_bp = Blueprint("productos", __name__)


@producto_bp.route("/")
def productos():
    return jsonify({"msg": "test"}), 200

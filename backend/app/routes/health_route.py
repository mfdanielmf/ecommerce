from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/")
def health_status():
    return jsonify({"msg": "OK"}), 200

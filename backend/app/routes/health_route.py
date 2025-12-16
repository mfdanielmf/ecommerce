from flask import Blueprint, jsonify
from flask_cors import cross_origin

health_bp = Blueprint("health", __name__)


@health_bp.route("/")
@cross_origin()
def health_status():
    return jsonify({"msg": "OK"}), 200

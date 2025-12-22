from flask import Blueprint

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    pass


@auth_bp.route("/register", methods=["POST"])
def register():
    pass

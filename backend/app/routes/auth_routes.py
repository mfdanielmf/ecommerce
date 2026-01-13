from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies
from app.models.usuario import Usuario
from app.services.auth_services import validar_usuario, comprobar_login
from app.models.exceptions import CampoIncorrectoException, CorreoYaUsadoException, NombreYaUsadoException, UsuarioNoExistenteException
from app.services.user_services import buscar_usuario_id, insertar_usuario_base

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("contraseña"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        usuario = comprobar_login(data)

        token = create_access_token(identity=str(
            usuario.id), additional_claims={"rol": usuario.rol})

        response = make_response(jsonify({
            "msg": "Has iniciado sesión correctamente",
            "usuario": usuario.to_dict()
        }), 200)

        set_access_cookies(response, token)

        return response

    except CampoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("correo") or not data.get("contraseña") or not data.get("contraseña_repetir"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        usuario: Usuario = validar_usuario(data)

        usuario_insertado: Usuario = insertar_usuario_base(usuario)

        return jsonify({
            "msg": "Usuario registrado correctamente",
            "usuario": usuario_insertado.to_dict()
        }), 200

    except CampoIncorrectoException:
        return jsonify({"error": "Algún campo introducido es incorrecto"}), 422
    except NombreYaUsadoException:
        return jsonify({"error": "El nombre ya está en uso"}), 409
    except CorreoYaUsadoException:
        return jsonify({"error": "El correo ya está en uso"}), 409


@auth_bp.route("/me")
@jwt_required()
def me():
    id_usuario = int(get_jwt_identity())

    try:
        usuario: Usuario = buscar_usuario_id(id_usuario)

        return jsonify({"usuario": usuario.to_dict()})
    except UsuarioNoExistenteException:
        return jsonify({"error": "Usuario no existe"}, 404)


@auth_bp.route("/logout", methods=["POST"])
def logout():
    # Devuelve 401 con un msg cuando no hay token
    resp = make_response(jsonify({"msg": "Sesión cerrada con éxito"}), 200)
    unset_jwt_cookies(resp)

    return resp

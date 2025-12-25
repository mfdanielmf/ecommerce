from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies
from app.repositories.user_repo import insert_user, find_user_id
from app.services.auth_services import validar_usuario, comprobar_login
from app.models.exceptions import ContraseñasDiferentesException, CorreoYaUsadoException, LongitudContraseñaIncorrectaException, LongitudNombreIncorrectaException, NombreYaUsadoException, UsuarioNoEncontradoException, ContraseñaIncorrectaException

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("contraseña"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        usuario = comprobar_login(data["nombre"], data["contraseña"])

        token = create_access_token(str(usuario.id))

        response = make_response(jsonify({
            "msg": "Has iniciado sesión correctamente",
            "token": token,
            "usuario": usuario.to_dict()
        }), 200)

        set_access_cookies(response, token)

        return response

    except LongitudNombreIncorrectaException:
        return jsonify({"error": "Longitud del nombre incorrecta"}), 422
    except LongitudContraseñaIncorrectaException:
        return jsonify({"error": "Longitud de la contraseña incorrecta"}), 422
    except UsuarioNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el usuario {data['nombre']}"}), 404
    except ContraseñaIncorrectaException:
        return jsonify({"error": "Contraseña incorrecta"}), 422


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("correo") or not data.get("contraseña") or not data.get("contraseña_repetir"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    nombre: str = data["nombre"]
    correo: str = data["correo"]
    contraseña: str = data["contraseña"]
    contraseña_repetir = data["contraseña_repetir"]

    try:
        usuario = validar_usuario(
            nombre, correo, contraseña, contraseña_repetir)

        usuario_insertado = insert_user(usuario)

        return jsonify({
            "msg": "Usuario registrado correctamente",
            "usuario": usuario_insertado.to_dict()
        }), 200

    except LongitudNombreIncorrectaException:
        return jsonify({"error": "Longitud del nombre incorrecta"}), 422
    except NombreYaUsadoException:
        return jsonify({"error": "El nombre ya está en uso"}), 409
    except CorreoYaUsadoException:
        return jsonify({"error": "El correo ya está en uso"}), 409
    except LongitudContraseñaIncorrectaException:
        return jsonify({"error": "Longitud de la contraseña incorrecta"}), 422
    except ContraseñasDiferentesException:
        return jsonify({"error": "Las contraseñas no son iguales"}), 422


@auth_bp.route("/me")
@jwt_required()
def me():
    id_usuario = int(get_jwt_identity())

    usuario = find_user_id(id_usuario)

    if not usuario:
        return jsonify({"error": "Usuario no existe"}, 404)

    return jsonify({"usuario": usuario.to_dict()})


@auth_bp.route("/logout", methods=["POST"])
def logout():
    # Devuelve 401 con un msg cuando no hay token
    resp = make_response(jsonify({"msg": "Sesión cerrada con éxito"}), 200)
    unset_jwt_cookies(resp)

    return resp

from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from app.repositories.user_repo import insert_user
from app.services.auth_services import validar_usuario, comprobar_login
from app.models.exceptions import ContraseñasDiferentesException, CorreoYaUsadoException, LongitudContraseñaIncorrectaException, LongitudNombreIncorrectaException, NombreYaUsadoException, UsuarioNoEncontradoException, ContraseñaIncorrectaException

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
@cross_origin()
def login():
    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("contraseña"):
        return jsonify({"error": "Faltan datos en la petición"}), 400

    try:
        usuario = comprobar_login(data["nombre"], data["contraseña"])

        return jsonify({"msg": "Has iniciado sesión correctamente", "usuario": usuario.to_dict()}), 200
    except LongitudNombreIncorrectaException:
        return jsonify({"error": "Longitud del nombre incorrecta"}), 422
    except LongitudContraseñaIncorrectaException:
        return jsonify({"error": "Longitud de la contraseña incorrecta"}), 422
    except UsuarioNoEncontradoException:
        return jsonify({"error": f"No se ha encontrado el usuario {data['nombre']}"}), 404
    except ContraseñaIncorrectaException:
        return jsonify({"error": "Contraseña incorrecta"}), 422


@auth_bp.route("/register", methods=["POST"])
@cross_origin()
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

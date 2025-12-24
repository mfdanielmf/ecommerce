import os
import jwt
from app.models.exceptions import CorreoYaUsadoException, UsuarioNoEncontradoException, ContraseñasDiferentesException, LongitudNombreIncorrectaException, NombreYaUsadoException, LongitudContraseñaIncorrectaException, ContraseñaIncorrectaException
from app.models.usuario import Usuario
from app.repositories.user_repo import find_user_id, find_user_name, find_user_correo


def validar_usuario(nombre: str, correo: str, contraseña: str, contraseña_repetir: str) -> Usuario | LongitudNombreIncorrectaException | NombreYaUsadoException | CorreoYaUsadoException | LongitudContraseñaIncorrectaException | ContraseñasDiferentesException:
    if len(nombre) < 4 or len(nombre) > 20:
        raise LongitudNombreIncorrectaException()

    if find_user_name(nombre):
        raise NombreYaUsadoException()

    if find_user_correo(correo):
        raise CorreoYaUsadoException()

    if len(contraseña) < 6:
        raise LongitudContraseñaIncorrectaException()

    if contraseña != contraseña_repetir:
        raise ContraseñasDiferentesException()

    return Usuario(nombre=nombre, correo=correo, contraseña=contraseña)


def comprobar_login(nombre: str, contraseña: str) -> Usuario | LongitudNombreIncorrectaException | LongitudContraseñaIncorrectaException | UsuarioNoEncontradoException | ContraseñaIncorrectaException:
    if len(nombre) < 4 or len(nombre) > 20:
        raise LongitudNombreIncorrectaException()

    if len(contraseña) < 6:
        raise LongitudContraseñaIncorrectaException()

    usuario = find_user_name(nombre)

    if not usuario:
        raise UsuarioNoEncontradoException()

    if not usuario.comprobar_contraseña(contraseña):
        raise ContraseñaIncorrectaException()

    return usuario


def comprobar_token(token: str) -> tuple[dict[str, any], int]:
    try:
        payload = jwt.decode(token, os.getenv(
            "JWT_SECRET_KEY"), algorithm=["HS256"])

        usuario = find_user_id(payload['id'])

        if not usuario:
            return {"error": "El usuario no existe"}, 401

        return {"usuario": usuario.to_dict()}
    except jwt.ExpiredSignatureError:
        return {"error": "La sesión ha expirado"}, 401
    except jwt.InvalidTokenError:
        return {"error": "Token inválido"}, 401
    except Exception:
        return {"error": "Error interno"}, 500

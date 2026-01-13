from app.models.exceptions import CampoIncorrectoException, CorreoYaUsadoException, NombreYaUsadoException
from app.models.usuario import Usuario
from app.repositories.user_repo import find_user_name, find_user_correo


def validar_usuario(data) -> Usuario | CampoIncorrectoException | NombreYaUsadoException | CorreoYaUsadoException:
    nombre: str = str(data["nombre"])
    correo: str = str(data["correo"])
    contraseña: str = str(data["contraseña"])
    contraseña_repetir: str = str(data["contraseña_repetir"])

    if len(nombre) < 4 or len(nombre) > 20 or len(contraseña) < 6 or contraseña != contraseña_repetir:
        raise CampoIncorrectoException()

    if find_user_name(nombre):
        raise NombreYaUsadoException()

    if find_user_correo(correo):
        raise CorreoYaUsadoException()

    return Usuario(nombre=nombre, correo=correo, contraseña=contraseña)


def comprobar_login(data) -> Usuario | CampoIncorrectoException:
    nombre: str = str(data["nombre"])
    contraseña: str = str(data["contraseña"])

    if len(nombre) < 4 or len(nombre) > 20 or len(contraseña) < 6:
        raise CampoIncorrectoException()

    usuario: Usuario = find_user_name(nombre)

    if not usuario:
        raise CampoIncorrectoException()

    if not usuario.comprobar_contraseña(contraseña):
        raise CampoIncorrectoException()

    return usuario

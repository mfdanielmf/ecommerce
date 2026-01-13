from app.models.exceptions import CampoIncorrectoException, CorreoYaUsadoException, UsuarioNoEncontradoException, LongitudNombreIncorrectaException, NombreYaUsadoException, LongitudContraseñaIncorrectaException, ContraseñaIncorrectaException
from app.models.usuario import Usuario
from app.repositories.user_repo import find_user_name, find_user_correo, insert_user


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


def comprobar_usuario_es_admin(data: str) -> bool:
    if not data or data["rol"] != "admin":
        return False

    return True


def insertar_usuario_base(usuario: Usuario) -> Usuario:
    usuario = insert_user(usuario)

    return usuario

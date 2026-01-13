from app.models.exceptions import UsuarioNoExistenteException
from app.models.usuario import Usuario
from app.repositories.user_repo import find_user_id, insert_user


def insertar_usuario_base(usuario: Usuario) -> Usuario:
    usuario: Usuario = insert_user(usuario)

    return usuario


def buscar_usuario_id(id: int) -> Usuario | UsuarioNoExistenteException:
    usuario: Usuario = find_user_id(id)

    if not usuario:
        raise UsuarioNoExistenteException()

    return usuario


def comprobar_usuario_es_admin(data: str) -> bool:
    if not data or data["rol"] != "admin":
        return False

    return True

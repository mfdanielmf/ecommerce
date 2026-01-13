
# PRODUCTOS
class ProductoNoEncontradoException(Exception):
    pass


# USUARIOS
class UsuarioNoExistenteException(Exception):
    pass


# AUTH
class ContraseñasDiferentesException(Exception):
    pass


class NombreYaUsadoException(Exception):
    pass


class CorreoYaUsadoException(Exception):
    pass


# CATEGORÍAS
class CategoriaNoEncontradaException(Exception):
    pass


class CategoriaYaExistenteException(Exception):
    pass


class CategoriaConProductosException(Exception):
    pass


# GENERAL
class CampoIncorrectoException(Exception):
    pass


class ErrorInternoException(Exception):
    pass

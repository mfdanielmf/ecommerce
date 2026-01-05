
# PRODUCTOS
class ProductoNoEncontradoException(Exception):
    pass


# AUTH
class ContraseñasDiferentesException(Exception):
    pass


class LongitudNombreIncorrectaException(Exception):
    pass


class NombreYaUsadoException(Exception):
    pass


class CorreoYaUsadoException(Exception):
    pass


class LongitudContraseñaIncorrectaException(Exception):
    pass


class UsuarioNoEncontradoException(Exception):
    pass


class ContraseñaIncorrectaException(Exception):
    pass


# CATEGORÍAS
class CategoriaNoEncontradaException(Exception):
    pass


# GENERAL
class CampoProductoIncorrectoException(Exception):
    pass


class ErrorInternoException(Exception):
    pass

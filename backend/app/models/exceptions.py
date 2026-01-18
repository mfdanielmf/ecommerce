
# PRODUCTOS
class ProductoNoEncontradoException(Exception):
    pass


# USUARIOS
class UsuarioNoExistenteException(Exception):
    pass


# AUTH
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


# PEDIDOS
class NoHayPedidosException(Exception):
    pass


class NoHayProductosException(Exception):
    pass


class PedidoNoEncontradoException(Exception):
    pass


class EstadoIncorrectoException(Exception):
    pass


class StockInsuficienteException(Exception):
    pass

# GENERAL


class CampoIncorrectoException(Exception):
    pass


class ErrorInternoException(Exception):
    pass

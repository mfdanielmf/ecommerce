from app.repositories.category_repo import get_all_categories, get_category_by_name
from app.models.categoria import Categoria
from app.models.exceptions import CategoriaNoEncontradaException


def obtener_todas_categorias() -> list[Categoria]:
    categorias = get_all_categories()

    return categorias


def obtener_categoria_por_nombre(nombre: str) -> Categoria | CategoriaNoEncontradaException:
    categoria = get_category_by_name(nombre)

    if not categoria:
        raise CategoriaNoEncontradaException()

    return categoria

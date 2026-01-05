from app.repositories.category_repo import get_all_categories
from app.models.categoria import Categoria


def obtener_todas_categorias() -> list[Categoria]:
    categorias = get_all_categories()

    return categorias

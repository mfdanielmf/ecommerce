from app.repositories.category_repo import get_all_categories, get_category_by_name, insert_category
from app.models.categoria import Categoria
from app.models.exceptions import CampoIncorrectoException, CategoriaNoEncontradaException, CategoriaYaExistenteException


def obtener_todas_categorias() -> list[Categoria]:
    categorias = get_all_categories()

    return categorias


def obtener_categoria_por_nombre(nombre: str) -> Categoria | CategoriaNoEncontradaException:
    categoria = get_category_by_name(nombre)

    if not categoria:
        raise CategoriaNoEncontradaException()

    return categoria


def insertar_categoria_base(data) -> Categoria | CampoIncorrectoException | CategoriaYaExistenteException:
    nombre: str = data["nombre"]
    descripcion: str = data["descripcion"]

    if len(nombre) < 1 or len(nombre) > 50 or len(descripcion) < 1 or len(descripcion) > 500:
        raise CampoIncorrectoException()

    # Si ya hay una categoría con el nombre, salimos
    categoria_base = get_category_by_name(nombre)

    if categoria_base:
        raise CategoriaYaExistenteException()

    categoria: Categoria = Categoria(nombre=nombre, descripcion=descripcion)

    categoria_final = insert_category(categoria)

    return categoria_final

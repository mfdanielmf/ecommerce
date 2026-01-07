from app.repositories.category_repo import get_all_categories, get_category_by_name, insert_category, get_category_by_id, delete_category, update_category
from app.models.categoria import Categoria
from app.models.exceptions import CampoIncorrectoException, CategoriaNoEncontradaException, CategoriaYaExistenteException, CategoriaConProductosException


def data_categoria_es_correcta(data) -> bool:
    nombre: str = data["nombre"]
    descripcion: str = data["descripcion"]

    if len(nombre) < 1 or len(nombre) > 50 or len(descripcion) < 1 or len(descripcion) > 500:
        return False

    return True


def obtener_todas_categorias() -> list[Categoria]:
    categorias = get_all_categories()

    return categorias


def obtener_categoria_por_id(id: int) -> Categoria | CategoriaNoEncontradaException:
    categoria = get_category_by_id(id)

    if not categoria:
        raise CategoriaNoEncontradaException()

    return categoria


def obtener_categoria_por_nombre(nombre: str) -> Categoria | CategoriaNoEncontradaException:
    categoria = get_category_by_name(nombre)

    if not categoria:
        raise CategoriaNoEncontradaException()

    return categoria


def insertar_categoria_base(data) -> Categoria | CampoIncorrectoException | CategoriaYaExistenteException:
    data_correcta = data_categoria_es_correcta(data)

    if not data_correcta:
        raise CampoIncorrectoException()

    nombre: str = data["nombre"]
    descripcion: str = data["descripcion"]

    # Si ya hay una categoría con el nombre, salimos
    categoria_base = get_category_by_name(nombre)

    if categoria_base:
        raise CategoriaYaExistenteException()

    categoria: Categoria = Categoria(nombre=nombre, descripcion=descripcion)

    categoria_final = insert_category(categoria)

    return categoria_final


def eliminar_categoria_base(id: int) -> CategoriaNoEncontradaException | CategoriaConProductosException:
    try:
        categoria: Categoria = obtener_categoria_por_id(id)

        if (categoria.productos):
            raise CategoriaConProductosException()

        delete_category(categoria)
    except CategoriaNoEncontradaException:
        raise CategoriaNoEncontradaException()


def actualizar_categoria(data, id: int) -> Categoria | CampoIncorrectoException | CategoriaNoEncontradaException | CategoriaYaExistenteException:
    data_correcta = data_categoria_es_correcta(data)

    if not data_correcta:
        raise CampoIncorrectoException()

    # Si el nombre ya está elegido, salimos
    categoria_base: Categoria = get_category_by_name(data["nombre"])

    if categoria_base:
        raise CategoriaYaExistenteException()

    try:
        categoria: Categoria = obtener_categoria_por_id(id)

        categoria.nombre = data["nombre"]
        categoria.descripcion = data["descripcion"]

        categoria_actualizada: Categoria = update_category(categoria)

        return categoria_actualizada
    except CategoriaNoEncontradaException:
        raise CategoriaNoEncontradaException()

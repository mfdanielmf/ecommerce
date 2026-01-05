from app.db.db import db
from app.models.categoria import Categoria


def get_all_categories() -> list[Categoria]:
    return Categoria.query.all()


def get_category_by_name(nombre: str) -> Categoria | None:
    return Categoria.query.filter_by(nombre=nombre).first()

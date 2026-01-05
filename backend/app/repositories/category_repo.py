from app.db.db import db
from app.models.categoria import Categoria


def get_all_categories() -> list[Categoria]:
    return Categoria.query.all()

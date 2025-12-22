from app.db.db import db
from app.models.usuario import Usuario


def find_user_id(id: int) -> Usuario | None:
    return Usuario.query.get(id)


def find_user_name(nombre: str) -> Usuario | None:
    return Usuario.query.filter_by(nombre=nombre).first()


def find_user_correo(correo: str) -> Usuario | None:
    return Usuario.query.filter_by(correo=correo).first()


def insert_user(usuario: Usuario) -> Usuario:
    db.session.add(usuario)
    db.session.commit()

    return usuario

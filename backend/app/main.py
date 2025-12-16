from decimal import Decimal
import os

from app.db.db import db
from app.models.producto import Producto
from app.routes.product_routes import producto_bp
from app.routes.health_route import health_bp
from flask import Flask

app = Flask(__name__)

app.register_blueprint(producto_bp, url_prefix="/api/productos")
app.register_blueprint(health_bp, url_prefix="/api/health")

app.secret_key = "Me da igual que veas la secret key de desarrollo"

# SQLAlchemy config
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
db_path = os.path.join(base_dir, "db", "store.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.cli.command("crear-tablas")
def crear_tablas():
    db.drop_all()
    db.create_all()

    URL = "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"

    productos_temporales = [
        Producto(
            nombre="Auriculares",
            descripcion="Sonido de alta calidad con cancelación de ruido.",
            precio=Decimal("129.99"),
            stock=50,
            img_url=URL,
        ),
        Producto(
            nombre="Teclado mecánico",
            descripcion="Switches rojos y hotswappable.",
            precio=Decimal("85.00"),
            stock=30,
            img_url=URL,
        ),
        Producto(
            nombre="Reloj inteligente",
            descripcion="Monitor de salud, notificaciones y llamadas.",
            precio=Decimal("299.00"),
            stock=15,
            img_url=URL,
        ),
        Producto(
            nombre="Disco duro",
            descripcion="2TB de capacidad SSD. Alta velocidad y muchas horas de vida útil.",
            precio=Decimal("45.50"),
            stock=75,
            img_url=URL,
        ),
        Producto(
            nombre="Cargador para el móvil",
            descripcion="Cargador portátil de carga rápida. Es universal (compatible con cualquier móvil)",
            precio=Decimal("35.99"),
            stock=100,
            img_url=URL,
        )
    ]

    db.session.add_all(productos_temporales)
    db.session.commit()
    print("Tablas creadas!!!")


if __name__ == "__main__":
    app.run('0.0.0.0', 8080, debug=True)

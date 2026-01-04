from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.config import config

from app.routes.product_routes import producto_bp
from app.routes.health_route import health_bp
from app.routes.auth_routes import auth_bp

from decimal import Decimal

from app.db.db import db
from flask_migrate import Migrate

from app.models.producto import Producto
from app.models.usuario import Usuario
from app.models.categoria import Categoria

app = Flask(__name__)

app.config.from_object(config["desarrollo"])

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app, origins="http://localhost:5173", supports_credentials=True)


app.register_blueprint(producto_bp, url_prefix="/api/productos")
app.register_blueprint(health_bp, url_prefix="/api/health")
app.register_blueprint(auth_bp, url_prefix="/auth")


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
    app.run('0.0.0.0', 8080)

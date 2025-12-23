import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("secret_key_dev")

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    db_path = os.path.join(base_dir, "db", "store.db")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Desarrollo(Config):
    DEBUG = True


class Produccion(Config):
    DEBUG = False


config = {
    "desarrollo": Desarrollo,
    "produccion": Produccion
}

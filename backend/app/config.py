from datetime import timedelta
import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY_DEV")

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    db_path = os.path.join(base_dir, "db", "store.db")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class Desarrollo(Config):
    DEBUG = True


class Produccion(Config):
    DEBUG = False


config = {
    "desarrollo": Desarrollo,
    "produccion": Produccion
}

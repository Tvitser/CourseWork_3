import base64
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))



class BaseConfig:
    SECRET_KEY = "you-will-never-guess"
    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 3

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000
    JSON_PATH = os.path.join(
        os.path.dirname(BASEDIR), "tests/fixtures.json"
    )

class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        os.path.dirname(BASEDIR), "database/project.db"
    )

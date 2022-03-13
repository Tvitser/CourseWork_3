import pytest

from project.config import TestingConfig, DevelopmentConfig
from project.server import create_app
from project.setup_db import db as database
from tests.services.test_genres_service import genre_dao_test
from tests.load_fixtures import load_fixtures_
#Делаем импорт в конфтест для использования в проекте

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        yield app


@pytest.fixture()
def db(app):
    database.init_app(app)
    load_fixtures_()
    yield database
    database.session.rollback()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client

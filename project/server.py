from flask import Flask, current_app
from flask_cors import CORS
from flask_restx import Api


from project.setup_db import db
from project.tools.functions import create_tables_
from project.views import genres_ns, movies_ns, directors_ns, auth_ns, users_ns, user_ns, favorites_ns

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    version="1.0",
    title="Flask Course Project 3",
    doc="/docs",
)

# Нужно для работы с фронтендом
cors = CORS()

def create_data(app):
    with app.app_context():
        create_tables_("Data", current_app.config['JSON_PATH'])

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)
    #api = Api(app)
    #api.init_app(app, add_specs=False)
    #api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(users_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorites_ns)
    #create_data(app)
    return app

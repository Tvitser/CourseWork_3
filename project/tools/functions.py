import json
import os

from project.setup_db import db
from project.models import *
from project.tools.security import get_password_hash
from sqlalchemy.exc import IntegrityError

def set_keys(req_json, inst_cls):
    inst_cls_keys = [key for key in inst_cls.__dict__.keys() if key != '_sa_instance_state']
    for k, v in req_json.items():
        #Проверка в принципе не нужна,
        # потому что Flask сам обработает,
        # если ключ в json отличный от схемы.
        if k in inst_cls_keys:
            setattr(inst_cls, k, v)


def read_json(filename, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def create_tables_(message, path):
    # user_service.create(data)
    # user = user_service.get_one(k)
    # tokens = JwtToken({'user_id': user.id, 'role': user.role}).get_tokens()
    # user_service.update(tokens, user.id)
    data = read_json(path)
    db.drop_all()
    db.create_all()
    user_movie = []
    users = []
    movies = []
    directors = []
    genres = []
    for item in data["user_movie"]:
        user_movie.append(User_Movie(**item))
    for item in data["users"]:
        item['password'] = get_password_hash(item.get("password"))
        users.append(User(**item))
    for item in data["movies"]:
        movies.append(Movie(**item))
    for item in data["directors"]:
        directors.append(Director(**item))
    for item in data["genres"]:
        genres.append(Genre(**item))
    try:
        db.session.add_all(user_movie)
        db.session.add_all(users)
        db.session.add_all(directors)
        db.session.add_all(movies)
        db.session.add_all(genres)
        db.session.commit()
    except IntegrityError as e:
        print(e)
    print(f"{message} already loaded!")
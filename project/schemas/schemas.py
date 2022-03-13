from marshmallow import Schema
from marshmallow.fields import Int, Str, Float, Pluck
from marshmallow_enum import EnumField

from project.services.enums import UserRole


class GenreSchema(Schema):
    id = Int(dump_only=True)
    name = Str(required=True)

class DirectorSchema(Schema):
    id = Int(dump_only=True)
    name = Str()

class MovieSchema(Schema):
    id = Int(dump_only=True)
    title = Str()
    description = Str()
    trailer = Str()
    year = Int()
    rating = Float()
    director = Pluck('DirectorSchema', "name", many=False)
    genre = Pluck('GenreSchema', "name", many=False)


class JwtSchema(Schema):
    user_id = Int(required=True)
    role = EnumField(UserRole, required=True)
    exp = Int()
    
class UserSchema(Schema):
    id = Int(dump_only=True)
    email = Str(required=True)
    name = Str(required=True)
    surname = Str()
    password = Str(load_only=True)
    role = EnumField(UserRole, required=True, default=UserRole.user)
    access_token = Str()
    refresh_token = Str()
    favourite_genre = Int()


class UserMovie(Schema):
    user_id = Int()
    movie_id = Int()
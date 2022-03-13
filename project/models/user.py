from project.models.base import BaseMixin
from project.services.enums import UserRole
from project.setup_db import db

class User(BaseMixin, db.Model):
    __tablename__ = 'user'
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    role = db.Column(db.Enum(UserRole))
    access_token = db.Column(db.String)
    refresh_token = db.Column(db.String)
    movie = db.relationship('Movie', secondary='user_movie', overlaps="user")
    favourite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))

    def __repr__(self):
        return f"<Movie '{self.name.title()}'>"
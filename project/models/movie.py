from project.models.base import BaseMixin
from project.setup_db import db


class Movie(BaseMixin, db.Model):
    __tablename__ = 'movie'
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")
    user = db.relationship('User', secondary='user_movie')

    def __repr__(self):
        return f"<Movie '{self.title.title()}'>"

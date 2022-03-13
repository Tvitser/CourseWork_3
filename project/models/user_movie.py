from project.setup_db import db


class User_Movie(db.Model):
    __tablename__ = 'user_movie'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)

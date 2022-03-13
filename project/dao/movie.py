import sqlalchemy

from project.models.user_movie import User_Movie
from project.models.movie import Movie
from project.exceptions import ItemNotFound


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        movie = self.session.query(Movie).get(bid)
        if not movie:
            raise ItemNotFound("Не найден Movie!")
        else:
            return movie

    def get_fav_user(self, user_id):
        return self.session.query(Movie).filter(User_Movie.movie_id == Movie.id, User_Movie.user_id == user_id)

    def get_all(self, page_size, page_index=1):
        return self.session.query(Movie).offset((int(page_index) - 1) * page_size).limit(None)

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def get_by_status(self, page_size=1, page_index=1):
        desc_expression = sqlalchemy.sql.expression.desc(Movie.year)
        return self.session.query(Movie).order_by(desc_expression).offset((int(page_index) - 1) * page_size).limit(
            page_size)

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, update):
        self.session.add(update)
        self.session.commit()

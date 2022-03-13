from project.dao.director import DirectorDAO
from project.dao.genre import GenreDAO
from project.models import Director, Genre
from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.dao.user_movie import User_MovieDAO
from project.services.director_service import DirectorService
from project.services.genres_service import GenreService
from project.services.movies_service import MovieService
from project.services.user import UserService
from project.services.user_movie_service import UserMovieService
from project.setup_db import db

director_dao = DirectorDAO(session=db.session, module=Director)
genre_dao = GenreDAO(session=db.session, module=Genre)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
user_movie_dao = User_MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
user_movie_service = UserMovieService(dao=user_movie_dao)
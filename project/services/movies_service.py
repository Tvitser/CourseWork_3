from project.dao.movie import MovieDAO
from project.tools.functions import set_keys


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_fav(self, user_id):
        return self.dao.get_fav_user(user_id)

    def get_all(self, filters, page_size, page_index=1):
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        elif filters.get("status") is not None:
            if filters.get("page") is not None:
                page_index = filters.get("page")
            movies = self.dao.get_by_status(page_size, page_index)
        else:
            movies = self.dao.get_all(page_size)
        return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, data, bid):
        update = self.dao.get_one(bid)
        set_keys(data, update)
        self.dao.update(update)

    def delete(self, rid):
        self.dao.delete(rid)

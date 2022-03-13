from project.dao.user_movie import User_MovieDAO


class UserMovieService:
    def __init__(self, dao: User_MovieDAO):
        self.dao = dao

    def create(self, data):
        return self.dao.create_user_movie(data)

    def delete(self, bid, movie_id):
        return self.dao.delete(bid, movie_id)
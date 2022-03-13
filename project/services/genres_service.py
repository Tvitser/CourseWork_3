from project.dao import GenreDAO
from project.services.base import BaseService


class GenreService(BaseService):
    def __init__(self, dao: GenreDAO):
        super().__init__(dao)
        self.dao = dao

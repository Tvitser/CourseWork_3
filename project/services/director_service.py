from project.dao.director import DirectorDAO
from project.services.base import BaseService


class DirectorService(BaseService):
    def __init__(self, dao: DirectorDAO):
        super().__init__(dao)
        self.dao = dao

from project.dao.base import BaseDAO


class GenreDAO(BaseDAO):
    def __init__(self, session, module):
        super().__init__(session, module)
        self.module = module
        self.session = session
from project.tools.functions import set_keys


class BaseService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    #Готовим update и только потом передаем в базу, решил на уровне базы не возится с data
    def update(self, data, bid):
        update = self.dao.get_one(bid)
        set_keys(data, update)
        return self.dao.update(update)

    def delete(self, rid):
        self.dao.delete(rid)

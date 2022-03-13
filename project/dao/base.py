from project.exceptions import ItemNotFound


class BaseDAO:
    def __init__(self, session, module):
        self.session = session
        self.module = module
        self.message = module.__name__

    def get_one(self, bid):
        director = self.session.query(self.module).get(bid)
        if not director:
            raise ItemNotFound(f"Не найден {self.message}!")
        else:
            return director

    def get_all(self):
        return self.session.query(self.module).all()

    def create(self, data):
        ent = self.module(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        data = self.get_one(rid)
        self.session.delete(data)
        self.session.commit()

    def update(self, update):
        self.session.add(update)
        self.session.commit()

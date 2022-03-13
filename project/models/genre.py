from project.models.base import BaseMixin
from project.setup_db import db


class Genre(BaseMixin, db.Model):
    __tablename__ = 'genre'
    name = db.Column(db.String(255))

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"

from project.dao.user import UserDAO
from project.tools.functions import set_keys
from project.tools.security import get_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_user(bid)

    def get_by_name(self, username):
        user = self.dao.get_user_by_name(username)
        return user

    def get_by_email(self, email):
        user = self.dao.get_user_by_email(email)
        return user

    def get_by_username_role(self, username, role):
        user = self.dao.get_user_and_role(username, role)
        return user

    def get_all(self, data):
        role = data.get('role')
        username = data.get('username')
        if role:
            users = self.dao.get_all_users_by_role(role)
            return users
        if username:
            return self.get_by_name(username)
        users = self.dao.get_all_users()
        return users

    def create(self, data):
        data["password"] = get_password_hash(data.get("password"))
        return self.dao.create_user(data)

    def update(self, data, bid):
        if data.get("password"):
            data["password"] = get_password_hash(data.get("password"))
        update = self.get_one(bid)
        set_keys(data, update)
        self.dao.update(update)

    def update_password(self, data, bid):
        data["password"] = get_password_hash(data.get("password"))
        update = self.get_one(bid)
        set_keys(data, update)
        self.dao.update(update)

    def delete(self, rid):
        self.dao.delete(rid)


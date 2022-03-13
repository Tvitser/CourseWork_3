from project.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        all_users = self.session.query(User)
        return all_users.all()


    def get_user_by_email(self, email):
        user = self.session.query(User).filter(User.email == email).one_or_none()
        return user

    def get_user_by_name(self, name):
        user = self.session.query(User).filter(User.username == name).one_or_none()
        return user

    def get_user_and_role(self, name, role):
        user = self.session.query(User).filter(User.username == name, User.role == role)
        return user

    def get_all_users_by_role(self, role):
        all_users = self.session.query(User).filter(User.role == role)
        return all_users

    def get_user(self, uid):
        user = self.session.query(User).get(uid)
        return user

    def create_user(self, data):
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, update):
        self.session.add(update)
        self.session.commit()

    def delete(self, bid):
        user = self.get_user(bid)
        self.session.delete(user)
        self.session.commit()

from abc import ABC


class AbstractUser(ABC):
    def __init__(self, username, first_name, last_name, verified=False):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.verified = verified

    def get_username(self):
        pass
    
    def get_fullname(self):
        pass

    def is_verified(self):
        pass

    def to_json(self):
        pass


class User(AbstractUser):
    def get_username(self):
        return self.username

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def is_verified(self):
        return self.verified

    def to_json(self):
        return self.__dict__
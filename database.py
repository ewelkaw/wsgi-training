from models.user import User


class Database:
    def __init__(self):
        self.users = [
            User("user1", "email1"),
            User("user2", "email2"),
            User("user3", "email3"),
        ]

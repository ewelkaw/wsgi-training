class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def get_all(cls, ctx):
        return ctx.database.users

    @classmethod
    def insert(cls, user, ctx):
        ctx.database.users.append(user)

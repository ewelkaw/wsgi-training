from typing import NamedTuple


class User(NamedTuple):
    username: str
    email: str

    @classmethod
    def get_all(cls, ctx):
        return ctx.database.users

    @classmethod
    def insert(cls, user, ctx):
        ctx.database.users.append(user)

from venv import create
from models.user import User
from context import Context
from database import Database
from views_register import ViewsRegister


class MockedInput:
    def __init__(self, string):
        self.string = string.encode()

    def read(self):
        return self.string


def test_user_model():
    input = MockedInput("username=ewelina&email=ewelina@gmail.com")
    views_storage = ViewsRegister()
    mock_db = Database()

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "POST",
        "QUERY_STRING": "",
        "PATH_INFO": "/users",
    }

    ctx = Context(env, views_storage, mock_db)
    users_count = len(User.get_all(ctx))
    user = User("ewelina", "ewelina@gmail.com")
    User.insert(user, ctx)
    all_users = User.get_all(ctx)
    assert len(all_users) == users_count + 1
    assert all_users[-1] == user

from context import Context
from database import Database
from controllers.users_controller import UsersController
from views_register import ViewsRegister

from models.user import User


class MockedInput:
    def __init__(self, string):
        self.string = string.encode()

    def read(self):
        return self.string


def test_adding_users():
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

    previous_users_count = len(mock_db.users)

    UsersController(ctx).create()
    assert len(mock_db.users) == previous_users_count + 1
    assert mock_db.users[-1] == User("ewelina", "ewelina@gmail.com")


def test_adding_user_failure():
    input = MockedInput("user=ewelina&mail=ewelina@gmail.com")
    views_storage = ViewsRegister()
    mock_db = Database()

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "POST",
        "QUERY_STRING": "",
        "PATH_INFO": "/users",
    }

    ctx = Context(env, views_storage, mock_db)

    previous_users_count = len(mock_db.users)

    UsersController(ctx).create()
    assert len(mock_db.users) == previous_users_count

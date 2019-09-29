from context import Context
from database import Database
from views_register import ViewsRegister


class MockedInput:
    def __init__(self, string):
        self.string = string.encode()

    def read(self):
        return self.string


def test_context():
    input = MockedInput("")

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "GET",
        "QUERY_STRING": "",
        "PATH_INFO": "/",
    }

    ctx = Context(env, "ViewsRegister", "Database")
    assert ctx.method == "GET"
    assert ctx.query_string == ""
    assert ctx.body == ""
    assert ctx.uri == "/"
    assert ctx.views_storage == "ViewsRegister"
    assert ctx.database == "Database"


def test_context_with_param():
    input = MockedInput("param=123&param2=234")

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "POST",
        "QUERY_STRING": "",
        "PATH_INFO": "/",
    }

    ctx = Context(env, "ViewsRegister", "Database")
    assert ctx.body == "param=123&param2=234"
    assert ctx.method == "POST"
    assert ctx.params == {"param": "123", "param2": "234"}


def test_query_string_with_params():
    input = MockedInput("")

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "GET",
        "QUERY_STRING": "param=123&param2=234",
        "PATH_INFO": "/",
    }

    ctx = Context(env, "ViewsRegister", "Database")
    assert ctx.method == "GET"
    assert ctx.params == {"param": "123", "param2": "234"}

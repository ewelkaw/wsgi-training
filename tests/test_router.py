from router import Router
from context import Context


class MockController:
    def __init__(self, ctx):
        pass

    def index(self):
        return "TEST"


class MockedInput:
    def __init__(self, string):
        self.string = string.encode()

    def read(self):
        return self.string


def test_basic_router():
    ROUTES = [("/", "GET", (MockController, "index"))]
    input = MockedInput("")

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "GET",
        "QUERY_STRING": "",
        "PATH_INFO": "/",
    }

    ctx = Context(env, "ViewsRegister", "Database")
    router = Router(ctx, ROUTES)
    code, action = router.call()
    assert code == 200
    assert action() == "TEST"


def test_404_router():
    ROUTES = []
    input = MockedInput("")

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "GET",
        "QUERY_STRING": "",
        "PATH_INFO": "/",
    }

    ctx = Context(env, "ViewsRegister", "Database")
    router = Router(ctx, ROUTES)
    code, _ = router.call()
    assert code == 404

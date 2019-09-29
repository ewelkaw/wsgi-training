from router import Router
from context import Context

from database import Database

from controllers.main_controller import MainController
from controllers.users_controller import UsersController
from views_register import ViewsRegister
from typing import Iterator, Callable, Any

STATUS_CODES = {200: "200 OK", 404: "404 Not found"}

ROUTES = [
    ("/", "GET", (MainController, "index")),
    ("/users", "GET", (UsersController, "index")),
    ("/users", "POST", (UsersController, "create")),
]

VIEWS_STORAGE = ViewsRegister()

MOCK_DB = Database()


def application(env: dict, start_response: Callable) -> Iterator[Any]:
    ctx = Context(env, VIEWS_STORAGE, MOCK_DB)

    router = Router(ctx, ROUTES)
    status, action = router.call()

    start_response(STATUS_CODES[status], [("Content-Type", "text/html")])

    yield action().encode()

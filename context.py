from database import Database
from views_register import ViewsRegister


class Context:
    def __init__(self, env: dict, views_storage: ViewsRegister, database: Database):
        self.method = env["REQUEST_METHOD"]
        self.query_string = env["QUERY_STRING"]
        self.body = env["wsgi.input"].read().decode("utf-8")
        self.uri = env["PATH_INFO"]
        self.views_storage = views_storage
        self.database = database

    @property
    def params(self) -> dict:
        if self.query_string == "" and self.body == "":
            return {}
        return dict(
            map(lambda x: x.split("="), (self.query_string or self.body).split("&"))
        )

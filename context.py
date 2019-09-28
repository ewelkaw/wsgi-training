class Context:
    def __init__(self, env, views_storage, database):
        self.method = env["REQUEST_METHOD"]
        self.query_string = env["QUERY_STRING"]
        self.body = env["wsgi.input"].read().decode("utf-8")
        self.uri = env["PATH_INFO"]
        self.views_storage = views_storage
        self.database = database

    @property
    def params(self):
        if self.query_string == "" and self.body == "":
            return {}
        return dict(
            map(lambda x: x.split("="), (self.query_string or self.body).split("&"))
        )


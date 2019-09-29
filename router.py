from controllers.system_controller import SystemController


class Router:
    def __init__(self, ctx, routes):
        self.ctx = ctx
        self.routes = routes

    def call(self) -> tuple:
        for route in self.routes:
            uri, method, (klass, action) = route
            if uri == self.uri and method == self.method:
                return (200, getattr(klass(self.ctx), action))
        return (404, SystemController(self.ctx).not_found)

    @property
    def uri(self) -> str:
        return self.ctx.uri

    @property
    def method(self) -> str:
        return self.ctx.method

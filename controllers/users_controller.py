from controllers.controller import Controller
from models.user import User
from jinja2 import Template


class UsersController(Controller):
    def index(self) -> Template:
        users = User.get_all(self.ctx)
        return self.render({"users": users}, "users/index.html")

    def create(self) -> Template:
        if self.ctx.params.get("username") and self.ctx.params.get("email"):
            u = User(self.ctx.params["username"], self.ctx.params["email"])
            User.insert(u, self.ctx)

        users = User.get_all(self.ctx)
        return self.render({"users": users}, "users/index.html")

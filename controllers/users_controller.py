from controllers.controller import Controller
from models.user import User

import time


class UsersController(Controller):
    def index(self):
        users = User.get_all(self.ctx)
        return self.render({"users": users}, "users/index.html")

    def create(self):
        if self.ctx.params.get("username") and self.ctx.params.get("email"):
            u = User(self.ctx.params["username"], self.ctx.params["email"])
            User.insert(u, self.ctx)

            users = User.get_all(self.ctx)
            return self.render({"users": users}, "users/index.html")

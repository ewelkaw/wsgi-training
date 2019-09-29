from controllers.controller import Controller
from jinja2 import Template


class MainController(Controller):
    def index(self) -> Template:
        return self.render(self.ctx.params, "main/index.html")

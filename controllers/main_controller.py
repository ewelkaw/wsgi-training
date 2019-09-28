from controllers.controller import Controller


class MainController(Controller):
    def index(self):
        return self.render(self.ctx.params, "main/index.html")

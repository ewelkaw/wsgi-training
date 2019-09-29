from controllers.controller import Controller


class SystemController(Controller):
    def not_found(self):
        return "Not found"

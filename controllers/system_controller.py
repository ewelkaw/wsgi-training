from controllers.controller import Controller


class SystemController(Controller):
    def not_found(self) -> str:
        return "Not found"

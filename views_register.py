from pathlib import Path


class ViewsRegister:
    def __init__(self):
        self.storage = {}

    def get(self, template_name: str) -> str:
        if template_name in self.storage:
            return self.storage[template_name]

        template_path = (
            Path(__file__).parent.absolute().joinpath("views/", template_name)
        )

        # not sure if it would work properly
        # in threaded env
        with open(template_path) as f:
            template = f.read()

        self.storage[template_name] = template

        return template

from pathlib import Path
from jinja2 import Template


class Controller:
    def __init__(self, ctx):
        self.ctx = ctx

    def render(self, render_ctx, template_name):
        return Template(self.ctx.views_storage.get(template_name)).render(render_ctx)


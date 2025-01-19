from pathlib import Path
from docutils import nodes
from sphinx.util.docutils import SphinxRole

class DiscreetRole(SphinxRole):
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        return [nodes.emphasis(text=self.text, classes=['discreet'])], []

def setup(app):
    app.add_html_theme('bridge_theme', Path(__file__).resolve().parent)
    app.add_role('discreet', DiscreetRole())

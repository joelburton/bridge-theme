from pathlib import Path
from docutils import nodes
from sphinx.util.docutils import SphinxRole
from sphinx.application import Sphinx

class DiscreetRole(SphinxRole):
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        return [nodes.emphasis(text=self.text, classes=['discreet'])], []

def setup(app: Sphinx):
    app.add_html_theme('bridge_theme', str(Path(__file__).resolve().parent))
    app.add_role('discreet', DiscreetRole())
    app.add_js_file('fix-page-toc.js')

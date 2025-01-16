from pathlib import Path

def setup(app):
    app.add_html_theme('bridge_theme', Path(__file__).resolve().parent)
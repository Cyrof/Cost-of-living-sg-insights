import os.path

import plotly.io
from flask import current_app as flask_app
from plotly.graph_objects import Figure

CHARTS_DIR: str = "data/charts"


def load_chart_json(filename: str) -> Figure:
    with flask_app.open_resource(os.path.join(CHARTS_DIR, filename)) as file:
        return plotly.io.from_json(file.read())

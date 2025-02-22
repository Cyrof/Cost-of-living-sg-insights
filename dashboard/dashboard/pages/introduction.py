import dash
import plotly.express as px
from dash import dcc, html

dash.register_page(__name__, path="/")


def layout():
    test_data: dict[str, list[int]] = {
        "x": list(range(0, 10)),
        "y": list(range(0, 10)),
    }

    return html.Div(
        [
            html.H1("Introduction"),
            dcc.Graph(id="graph-content", figure=px.line(test_data, x="x", y="y")),
        ]
    )

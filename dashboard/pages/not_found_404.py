import dash
import plotly.express as px
from dash import dcc, html

dash.register_page(__name__)


def layout():
    return html.Div(
        [
            html.H1("404 - Not found"),
        ]
    )

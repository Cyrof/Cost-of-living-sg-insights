import dash
from dash import html

dash.register_page(__name__)


def layout():
    return html.Div([html.H1("Taxes")])

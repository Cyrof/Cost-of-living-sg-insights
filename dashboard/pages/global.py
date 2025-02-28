import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure

import dashboard.utils

dash.register_page(__name__)


def load_charts() -> dict[str, Figure]:
    return {
        "cpi_bubble_map": dashboard.utils.load_chart_json("cpi_bubble_map.json"),
        "gdp_bubble_map": dashboard.utils.load_chart_json("gdp_bubble_map.json"),
        "cpi_vs_gdp_bubble_chart": dashboard.utils.load_chart_json(
            "cpi_vs_gdp_bubble_chart.json"
        ),
    }


def layout() -> Component:
    charts: dict[str, Figure] = load_charts()

    return html.Div(
        [
            html.H1("Global"),
            dcc.Graph(id="cpi_bubble_map", figure=charts["cpi_bubble_map"]),
            dcc.Graph(id="gdp_bubble_map", figure=charts["gdp_bubble_map"]),
            dcc.Graph(
                id="cpi_vs_gdp_bubble_chart", figure=charts["cpi_vs_gdp_bubble_chart"]
            ),
        ]
    )

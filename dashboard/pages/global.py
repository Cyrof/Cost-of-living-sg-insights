import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper

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
    return dmc.Stack(
        [
            dmc.Stack(
                [
                    dmc.Text(
                        "Global",
                        className="text-3xl font-semibold"
                    ),
                    dmc.Stack(
                        [
                            dmc.Text(
                                "cpi & gdp text",
                                className="border border-purple-500"
                            ),
                            dmc.Group(
                                gap="lg",
                                grow=True,
                                children=[
                                    graphWrapper(
                                        id="cpi_bubble_map",
                                        figure=charts["cpi_bubble_map"]
                                    ),
                                    graphWrapper(
                                        id="gdp_bubble_map",
                                        figure=charts["gdp_bubble_map"]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            ),
            dmc.Stack(
                [
                    dmc.Text(
                        "cpi vs gdp text",
                        className="border border-cyan-500"
                    ),
                    graphWrapper(
                        id="cpi_vs_gdp_bubble_chart",
                        figure=charts["cpi_vs_gdp_bubble_chart"]
                    )
                ],
                className="mt-12"
            )
        ],
        className="py-2 px-4"
    )
import dash
import dash_mantine_components as dmc
from dash.development.base_component import Component
from plotly.graph_objects import Figure

import dashboard.utils
from dashboard.components.textComponents import (create_card_graph,
                                                 create_page_title,
                                                 create_section_title)
from dashboard.text.globalText import *

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_global_charts()
    return dmc.Stack(
        className="w-full",
        gap="md",
        children=[
            create_page_title(
                "Singapore and the Globe",
                "Comparing Singapore's economy with other countries'",
            ),
            create_section_title(
                "How does Singapore's CPI and GDP compare with other countries?"
            ),
            create_card_graph(
                title="Geographical Plot of CPI and GDP",
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(CPI_OVER_TIME_SHORT_1),
                                dmc.ListItem(CPI_OVER_TIME_SHORT_2),
                                dmc.ListItem(CPI_OVER_TIME_SHORT_3),
                                dmc.ListItem(GDP_OVER_TIME_SHORT_1),
                                dmc.ListItem(GDP_OVER_TIME_SHORT_2),
                                dmc.ListItem(GDP_OVER_TIME_SHORT_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(CPI_OVER_TIME_1),
                        dmc.Text(CPI_OVER_TIME_2),
                        dmc.Text(GDP_OVER_TIME_1),
                        dmc.Text(GDP_OVER_TIME_2),
                    ]
                ),
                graphs=[
                    ("cpi_bubble_map", charts["cpi_bubble_map"]),
                    ("gdp_bubble_map", charts["gdp_bubble_map"]),
                ],
            ),
            create_card_graph(
                title="Bubble Chart of CPI and GDP",
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(CPI_GDP_OVER_TIME_SHORT_1),
                                dmc.ListItem(CPI_GDP_OVER_TIME_SHORT_2),
                                dmc.ListItem(CPI_GDP_OVER_TIME_SHORT_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(CPI_GDP_OVER_TIME_1),
                        dmc.Text(CPI_GDP_OVER_TIME_2),
                        dmc.Text(CPI_GDP_OVER_TIME_3),
                    ]
                ),
                graphs=[("cpi_vs_gdp_bubble_chart", charts["cpi_vs_gdp_bubble_chart"])],
            ),
            dmc.Divider(),
            # recommendation
            create_section_title("Our Recommendations"),
            dmc.Stack(
                [
                    dmc.Text(GLOBAL_RECO_1),
                    dmc.Text(GLOBAL_RECO_2),
                ]
            ),
        ],
    )

import dash
import dash_mantine_components as dmc
from dash.development.base_component import Component
from plotly.graph_objects import Figure
from text.globalText import *

import dashboard.utils
from dashboard.components.textComponents import (create_card_graph,
                                                 create_page_title,
                                                 create_section_title)

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
                short_desc=CPI_OVER_TIME_Short + GDP_OVER_TIME_Short,
                full_desc=CPI_GDP_OVER_TIME + GDP_OVER_TIME,
                graphs=[
                    ("cpi_bubble_map", charts["cpi_bubble_map"]),
                    ("gdp_bubble_map", charts["gdp_bubble_map"]),
                ],
            ),
            create_card_graph(
                title="Bubble Chart of CPI and GDP",
                short_desc=CPI_GDP_OVER_TIME_Short,
                full_desc=CPI_GDP_OVER_TIME,
                graphs=[("cpi_vs_gdp_bubble_chart", charts["cpi_vs_gdp_bubble_chart"])],
            ),
            dmc.Divider(),
            # recommendation
            create_section_title("Our Recommendations"),
            dmc.Text(GLOBAL_RECO),
        ],
    )

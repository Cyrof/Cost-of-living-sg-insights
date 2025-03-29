import dash
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc
from dashboard.components.graphWrapper import graphWrapper
from dashboard.components.textComponents import (
    create_card,
    create_section_title,
    create_card_graph,
)
from text.globalText import *

import dashboard.utils

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_global_charts()
    return dmc.Stack(
        [
            # header
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Title(
                            "Global Dashboard",
                            className="text-4xl font-extrabold text-center",
                        ),
                        dmc.Title(
                            "Tracking Worldwide Economic Trends",
                            order=2,
                            className="text-xl font-medium text-center opacity-80",
                        ),
                    ],
                    gap="xs",
                    className="py-6",
                ),
                className="rounded-xl mb-8 shadow-lg w-full",
                withBorder=False,
            ),
            # CPI and GDP
            create_section_title("Regional Economic Overview on CPI & GDP"),
            create_card_graph(
                title="Neighbouring Economies: CPI & GDP",
                short_desc=CPI_OVER_TIME_Short + GDP_OVER_TIME_Short,
                full_desc=CPI_GDP_OVER_TIME + GDP_OVER_TIME,
                graphs=[
                    ("cpi_bubble_map", charts["cpi_bubble_map"]),
                    ("gdp_bubble_map", charts["gdp_bubble_map"]),
                ],
            ),
            # CPI VS GDP
            create_section_title("CPI and GDP Bubble Analysis"),
            create_card_graph(
                title="Neighbouring Economies: CPI VS GDP",
                short_desc=CPI_GDP_OVER_TIME_Short,
                full_desc=CPI_GDP_OVER_TIME,
                graphs=[("cpi_vs_gdp_bubble_chart", charts["cpi_vs_gdp_bubble_chart"])],
            ),
            # recommendation
            create_section_title("Strategic Recommendations"),
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Text(
                            "Expert Recommendation",
                            className="text-2xl font-bold",
                        ),
                        dmc.Divider(
                            className="my-2", size="sm"
                        ),
                        dmc.Text(
                            GLOBAL_RECO,
                            className="text-base font-normal leading-relaxed",
                        ),
                    ],
                    className="p-6",
                ),
                shadow="sm",
                radius="lg",
                className="transition-all duration-300 hover:shadow-xl mt-2 mb-12 w-full",
                withBorder=True,
                style={"borderWidth": "2px"},
            ),
        ],
        className="p-8 w-full",
        gap="md",
    )

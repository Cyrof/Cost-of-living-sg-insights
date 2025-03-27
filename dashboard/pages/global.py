import dash
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper
from components.textComponents import create_card, create_section_title
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
                        dmc.Text(
                            "Global Dashboard",
                            className="text-4xl font-extrabold text-palette4 text-center"
                        ),
                        dmc.Text(
                            "Tracking Worldwide Economic Trends",
                            className="text-xl font-medium text-palette3 text-center opacity-80"
                        )
                    ],
                    gap="xs",
                    className="py-6"
                ),
                className="bg-palette1 rounded-xl mb-8 shadow-lg w-full",
                withBorder=False,
            ),
            # CPI and GDP
            create_section_title("Regional Economic Overview on CPI & GDP"),
            dmc.Stack(
                [
                    create_card(
                        "Neighbouring Economies: CPI & GDP",
                        CPI_GDP_OVER_TIME + GDP_OVER_TIME,
                        "w-full"
                    ),
                    dmc.Group(
                        gap="xl",
                        grow=True,
                        className="h-[28rem] w-full",
                        children=[
                            dmc.Paper(
                                graphWrapper(
                                    id="cpi_bubble_map",
                                    figure=charts["cpi_bubble_map"]
                                ),
                                shadow="sm",
                                radius="lg",
                                className="w-3/5 transition-all duration-300 hover:shadow-xl",
                                withBorder=True,
                                style={
                                    "borderColor": "var(--palette3)",
                                    "borderWidth": "2px"
                                }
                            ),
                            dmc.Paper(
                                graphWrapper(
                                    id="gdp_bubble_map",
                                    figure=charts["gdp_bubble_map"]
                                ),
                                shadow="sm",
                                radius="lg",
                                className="w-3/5 transition-all duration-300 hvoer:shadow-xl",
                                withBorder=True,
                                style={
                                    "borderColor": "var(--palette3)",
                                    "borderWidth": "2px"
                                }
                            )
                        ]
                    )
                ],
                className="w-full"
            ),
            # CPI VS GDP
            create_section_title("CPI and GDP Bubble Analysis"),
            dmc.Stack(
                [
                    create_card(
                        "Neighbouring Economies: CPI VS GDP",
                        CPI_GDP_OVER_TIME,
                        "w-full"
                    ),
                    dmc.Paper(
                        graphWrapper(
                            id="cpi_vs_gdp_bubble_chart",
                            figure=charts["cpi_vs_gdp_bubble_chart"]
                        ),
                        shadow="sm",
                        radius="lg",
                        className="w-full transition-all durationn-300 hover:shadow-xl",
                        withBorder=True,
                        style={
                            "borderColor": "var(--palette3)",
                            "borderWidth": "2px"
                        }
                    )
                ],
                className="p-6"
            ),
            # recommendation
            create_section_title("Strategic Recommendations"),
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Text(
                            "Expert Recommendation",
                            className="text-2xl font-bold text-palette3"
                        ),
                        dmc.Divider(
                            className="my-2",
                            color="var(--palette3)",
                            size="sm"
                        ),
                        dmc.Text(
                            GLOBAL_RECO,
                            className="pl-6 text-base font-normal leading-relaxed text-palette3"
                        )
                    ],
                    className="p-6"
                ),
                shadow="sm",
                radius="lg",
                className="bg-white transition-all duration-300 hover:shadow-xl mt-2 mb-12 w-full",
                withBorder=True,
                style={
                    "borderColor": "var(--palette3)",
                    "borderWidth": "2px"
                }
            )
        ],
        className="p-8 w-full",
        gap="md"
    )

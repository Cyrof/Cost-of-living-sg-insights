import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper
from components.textComponents import create_card, create_section_title
from text.healthcareText import *

import dashboard.utils

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_healthcare_charts()
    return dmc.Stack(
        [
            # header
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Text(
                            "Healthcare Dashboard",
                            className="text-4xl font-extrabold text-palette4 text-center"
                        ),
                        dmc.Text(
                            "Uncovering insights into healthcare costs and market dynamics",
                            className="text-xl font-medium text-palette3 text-center opacity-80"
                        )
                    ],
                    gap="xs",
                    className="py-6"
                ),
                className="bg-palette1 rounded-xl mb-8 shadow-lg w-full",
                withBorder=False,
            ),
            # healthcare breakdown
            create_section_title("Healthcare CPI Breakdown"),
            dmc.Stack(
                [
                    dmc.Group(
                        gap="xl",
                        grow=True,
                        children=[
                            create_card(
                                "Breakdown of Healthcare CPI",
                                HEALTHCARE_COM,
                                "w-1/2"
                            ),
                            dmc.Paper(
                                graphWrapper(
                                    id="healthcare_cpi_breakdown_chart",
                                    figure=charts["healthcare_cpi_breakdown"]
                                ),
                                shadow="sm",
                                radius="lg",
                                className="w-full transition-all duration-300 hover:shadow-xl",
                                withBorder=True,
                                style={
                                    "borderColor": "var(--palette3)",
                                    "borderWidth": "2px"
                                }
                            ),
                        ],
                        className="mt-2 h-[28rem] w-full"
                    ),
                ],
            ),
            # life expectancy vs healthcare & healthcare vs income
            create_section_title("Health & Income Insights"),
            dmc.SimpleGrid(
                cols=2,
                spacing="lg",
                children=[
                    dmc.Paper(
                        graphWrapper(
                            id="life_expectancy_vs_healthcare_cpi_chart",
                            figure=charts["life_expectancy_vs_healthcare_cpi"]
                        ),
                        shadow="sm",
                        radius="lg",
                        className="w-full transition-all duration-300 hover:shadow-xl",
                        withBorder=True,
                        style={
                            "borderColor": "var(--palette3)",
                            "borderWidth": "2px"
                        }
                    ),
                    dmc.Paper(
                        graphWrapper(
                            id="healthcare_cpi_vs_gross_monthly_income",
                            figure=charts["healthcare_cpi_vs_gross_monthly_income"]
                        ),
                        shadow="sm",
                        radius="lg",
                        className="w-full transition-all duration-300 hover:shadow-xl",
                        withBorder=True,
                        style={
                            "borderColor": "var(--palette3)",
                            "borderWidth": "2px"
                        }
                    ),
                    create_card(
                        "Life Expectancy VS Healthcare CPI",
                        LIFE_EXPECTANCY_HEALTHCARE,
                        "w-full"
                    ),
                    create_card(
                        "Healthcare CPI VS Income Growth",
                        HEALTHCARE_VS_INCOME,
                        "w-full"
                    ),
                ],
            ),
            # healthcare percentage 
            create_section_title("CPI and Income Growth Trends"),
            dmc.Stack(
                [
                    dmc.Group(
                        gap="lg",
                        grow=True,
                        children=[
                            dmc.Paper(
                                graphWrapper(
                                    id="percentage_change_in_healthcare_cpi_and_income_chart",
                                    figure=charts["percentage_change_in_healthcare_cpi_and_income"]
                                ),
                                shadow="sm",
                                radius="lg",
                                className="w-full transition-all duration-300 hover:shadow-xl",
                                withBorder=True,
                                style={
                                    "borderColor": "var(--palette3)",
                                    "borderWidth": "2px"
                                }
                            ),
                            create_card(
                                "Healthcare CPI VS Income Growth (%)",
                                HEALTHCARE_VS_INCOME_PERCENTAGE,
                                "w-1/2"
                            )
                        ],
                        className="mt-2 h-[28rem] w-full"
                    ),
                ],
            ),
            # recommendation 
            create_section_title("Strategic Recommendations"),
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Text(
                            "Expert Recommendations",
                            className="text-2xl font-bold text-palette3",
                        ),
                        dmc.Divider(
                            className="my-2",
                            color="var(--palette3)",
                            size="sm"
                        ),
                        dmc.Text(
                            HEALTHCARE_RECO,
                            className="pl-6 text-base font-normal leading-relaxed text-palette3"
                        )
                    ],
                    className="p-6"
                ),
                shadow="sm",
                radius="lg",
                className="bg-palette1 transition-all duration-300 hover:shadow-xl mt-2 mb-12 w-full",
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
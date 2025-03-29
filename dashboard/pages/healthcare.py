import dash
import dash_mantine_components as dmc
from dashboard.components.graphWrapper import graphWrapper
from dashboard.components.textComponents import (
    create_card,
    create_card_graph,
    create_section_title,
)
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
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
                        dmc.Title(
                            "Healthcare Dashboard",
                            className="text-4xl font-extrabold text-center",
                        ),
                        dmc.Title(
                            "Uncovering insights into healthcare costs and market dynamics",
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
            # healthcare breakdown
            create_section_title("Healthcare CPI Breakdown"),
            create_card_graph(
                title="Breakdown of Healthcare CPI",
                short_desc=HEALTHCARE_COM_Short,
                full_desc=HEALTHCARE_COM,
                # figure=charts["healthcare_cpi_breakdown"],
                # card_id="healthcare_cpi_breakdown_chart"
                graphs=[
                    (
                        "healthcare_cpi_breakdown_chart",
                        charts["healthcare_cpi_breakdown"],
                    )
                ],
            ),
            # life expectancy vs healthcare & healthcare vs income
            create_section_title("Health & Income Insights"),
            create_card_graph(
                title="Life Expectancy VS Healthcare CPI",
                short_desc=LIFE_EXPECTANCY_HEALTHCARE_Short,
                full_desc=LIFE_EXPECTANCY_HEALTHCARE,
                # figure=charts["life_expectancy_vs_healthcare_cpi"],
                # card_id="life_expectancy_vs_healthcare_cpi_chart",
                graphs=[
                    (
                        "life_expectancy_vs_healthcare_cpi_chart",
                        charts["life_expectancy_vs_healthcare_cpi"],
                    )
                ],
            ),
            create_card_graph(
                title="Healthcare CPI VS Income Growth",
                short_desc=HEALTHCARE_VS_INCOME_Short,
                full_desc=HEALTHCARE_VS_INCOME,
                graphs=[
                    (
                        "healthcare_cpi_vs_gross_monthly_income",
                        charts["healthcare_cpi_vs_gross_monthly_income"],
                    )
                ],
            ),
            # healthcare percentage
            create_section_title("CPI and Income Growth Trends"),
            create_card_graph(
                title="Healthcare CPI vs Income Growth (%)",
                short_desc=HEALTHCARE_VS_INCOME_PERCENTAGE_Short,
                full_desc=HEALTHCARE_VS_INCOME_PERCENTAGE,
                # figure=charts["percentage_change_in_healthcare_cpi_and_income"],
                # card_id="percentage_change_in_healthcare_cpi_and_income_chart",
                graphs=[
                    (
                        "percentage_change_in_healthcare_cpi_and_income_chart",
                        charts["percentage_change_in_healthcare_cpi_and_income"],
                    )
                ],
            ),
            # recommendation
            create_section_title("Strategic Recommendations"),
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Text(
                            "Expert Recommendations",
                            className="text-2xl font-bold",
                        ),
                        dmc.Divider(
                            className="my-2", size="sm"
                        ),
                        dmc.Text(
                            HEALTHCARE_RECO,
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

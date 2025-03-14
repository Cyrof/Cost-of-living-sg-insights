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
        "life_expectancy_vs_healthcare_cpi": dashboard.utils.load_chart_json(
            "life_expectancy_vs_healthcare_cpi.json"
        ),
        "healthcare_cpi_vs_gross_monthly_income": dashboard.utils.load_chart_json(
            "healthcare_cpi_vs_gross_monthly_income.json"
        ),
        "percentage_change_in_healthcare_cpi_and_income": dashboard.utils.load_chart_json(
            "percentage_change_in_healthcare_cpi_and_income.json"
        ),
        "healthcare_cpi_breakdown": dashboard.utils.load_chart_json(
            "healthcare_cpi_breakdown.json"
        ),
    }


def layout() -> Component:
    charts: dict[str, Figure] = load_charts()
    return dmc.Stack(
        [
            dmc.Stack(
                [
                    dmc.Text(
                        "Necessities",
                        className="text-3xl font-semibold"
                    ),
                    dmc.Group(
                        gap="lg",
                        grow=True,
                        children=[
                            dmc.Text(
                                "Healthcare Components text",
                                className="border border-purple-500"
                            ),
                            graphWrapper(
                                id="healthcare_cpi_breakdown_chart",
                                figure=charts["healthcare_cpi_breakdown"]
                            )
                        ]
                    )
                ]
            ),
            dmc.SimpleGrid(
                cols=2,
                spacing="lg",
                children=[
                    graphWrapper(
                        id="life_expectancy_vs_healthcare_cpi_chart",
                        figure=charts["life_expectancy_vs_healthcare_cpi"]
                    ),
                    graphWrapper(
                        id="healthcare_cpi_vs_gross_monthly_income",
                        figure=charts["life_expectancy_vs_healthcare_cpi"]
                    ),
                    dmc.Text(
                        "Life Expectancy vs Healthcare CPI text",
                        className="border border-orange-500"
                    ),
                    dmc.Text(
                        "Healthcare CPI vs Income Growth (%) text",
                        className="border border-green-500"
                    )
                ],
                className="mt-12"
            ),
            dmc.Group(
                gap="lg",
                grow=True,
                children=[
                    graphWrapper(
                        id="percentage_change_in_healthcare_cpi_and_income_chart",
                        figure=charts["percentage_change_in_healthcare_cpi_and_income"]
                    ),
                    dmc.Text(
                        "Healthcare CPI vs Income Growth",
                        className="border border-blue-500"
                    )
                ],
                className="mt-12"
            )
        ],
        className="py-2 px-4"
    )
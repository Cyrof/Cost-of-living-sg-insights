import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper

import dashboard.utils
from text.necessitiesText import *

dash.register_page(__name__)


def load_charts() -> dict[str, Figure]:
    return {
        "necessities_cpi_breakdown": dashboard.utils.load_chart_json(
            "necessities_cpi_breakdown.json"
        ),
        "necessities_cpi_vs_income": dashboard.utils.load_chart_json(
            "necessities_cpi_vs_income.json"
        ),
        "monthly_expenditure_donut": dashboard.utils.load_chart_json(
            "monthly_expenditure_donut.json"
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
                            dmc.Paper(
                                dmc.Text(
                                    NECESSITIES_CPI,
                                    className="text-xl font-medium text-palette3 p-6"
                                ),
                                shadow="sm",
                                radius="md",
                                className="mb-8 bg-palette1 h-full",
                                withBorder=True,
                                style={"borderColor": "var(--palette3)"}
                            ),
                            graphWrapper(
                                id="necessities_cpi_breakdown_chart",
                                figure=charts["necessities_cpi_breakdown"]
                            ),
                        ],
                    ),
                ]
            ),
            dmc.Stack(
                [
                    dmc.Text(
                        "CPI of Necessities against Income text",
                        className="border border-orange-500"
                    ),
                    graphWrapper(
                        id="necessities_cpi_vs_income_chart",
                        figure=charts["necessities_cpi_vs_income"]
                    ),
                ],
                className="mt-12"
            ),
            dmc.Group(
                gap="lg",
                grow=True,
                children=[
                    graphWrapper(
                        id="monthly_expenditure_donut_chart",
                        figure=charts["monthly_expenditure_donut"]
                    ),
                    dmc.Text(
                        "Month Expenditure over Time text",
                        className="border border-red-500"
                    )
                ],
                className="mt-12"
            )

        ],
        className="py-2 px-4"
    )

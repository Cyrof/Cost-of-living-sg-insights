import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper

import dashboard.utils
from text.necessitiesText import *
from components.textComponents import create_card, create_section_title

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
            # Header
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Text(
                            "Necessities Dashboard",
                            className="text-4xl font-extrabold text-palette4 text-center"
                        ),
                        dmc.Text(
                            "Tracking essential expenses and economic indicators",
                            className="text-xl font-medium text-palette3 text-center opacity-80"
                        )
                    ],
                    gap="xs",
                    className="py-6"
                ),
                className="bg-palette1 rounded-xl mb-8 shadow-lg w-full",
                withBorder=False,
            ),

            create_section_title("Cost of Living Trends"),
            dmc.Group(
                gap="xl",
                grow=True,
                className="h-[28rem] w-full",
                children=[
                    create_card(
                        "Breakdown CPI of Necessities Over Time",
                        NECESSITIES_CPI,
                        "w-2/5"
                    ),
                    dmc.Paper(
                        graphWrapper(
                            id="necessities_cpi_breakdown_chart",
                            figure=charts["necessities_cpi_breakdown"]
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
                ],
            ),

            # cpi vs income
            create_section_title("Income vs. Expenses Analysis"),
            dmc.Stack(
                [
                    create_card(
                        "CPI of Necessities Against Gross Monthly Income",
                        CPI_AGAINST_INCOME
                    ),
                    dmc.Paper(
                        graphWrapper(
                            id="necessities_cpi_vs_income_chart",
                            figure=charts["necessities_cpi_vs_income"]
                        ),
                        shadow="sm",
                        radius="lg",
                        className="mt-4 transition-all duration-300 hover:shadow-xl h-auto",
                        withBorder=True,
                        style={
                            "borderColor": "var(--palette3)",
                            "borderWidth": "2px"
                        }
                    ),
                ],
                className="mt-2 w-full",
            ),

            # Monthly Expenditure
            create_section_title("Monthly Expenditure Breakdown"),
            dmc.Group(
                gap="xl",
                grow=True,
                children=[
                    dmc.Paper(
                        graphWrapper(
                            id="monthly_expenditure_donut_chart",
                            figure=charts["monthly_expenditure_donut"]
                        ),
                        shadow="sm",
                        radius="lg",
                        className="w-1/2 transition-all duration-300 hover:shadow-xl h-auto",
                        withBorder=True,
                        style={
                            "borderColor": "var(--palette3)",
                            "borderWidth": "2px"
                        }
                    ),
                    create_card(
                        "Breakdown of Monthly Expenditure Over Time",
                        MONTHLY_EXPENDITURE,
                        "w-1/2"
                    ),
                ],
                className="mt-2 h-[28rem] w-full"
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
                        html.Ul(
                            [html.Li(point, className="mb-2 text-palette3")
                             for point in NECESSITIES_RECO.split('\n\n')],
                            className="list-disc pl-6 text-base font-normal leading-relaxed"
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
        gap="md",
    )

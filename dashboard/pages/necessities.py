import dash
from dash import html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper

import dashboard.utils
from text.necessitiesText import *
from components.textComponents import (
    create_card,
    create_section_title,
    create_card_graph,
)

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_necessities_charts()

    return dmc.Stack(
        [
            # Header
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Title(
                            "Necessities Dashboard",
                            className="text-4xl font-extrabold text-palette4 text-center",
                        ),
                        dmc.Title(
                            "Tracking essential expenses and economic indicators",
                            order=2,
                            className="text-xl font-medium text-palette3 text-center opacity-80",
                        ),
                    ],
                    gap="xs",
                    className="py-6",
                ),
                className="bg-palette1 rounded-xl mb-8 shadow-lg w-full",
                withBorder=False,
            ),
            create_section_title("Cost of Living Trends"),
            create_card_graph(
                title="Breakdown Necessities CPI Over Time",
                short_desc=NECESSITIES_CPI_Short,
                full_desc=NECESSITIES_CPI,
                graphs=[
                    (
                        "necessities_cpi_breakdown_chart",
                        charts["necessities_cpi_breakdown"],
                    )
                ],
            ),
            # cpi vs income
            create_section_title("Income vs. Expenses Analysis"),
            create_card_graph(
                title="CPI of Necessitiees Against Gross Monthly Income",
                short_desc=CPI_AGAINST_INCOME_Short,
                full_desc=CPI_AGAINST_INCOME,
                graphs=[
                    (
                        "necessities_cpi_vs_income_chart",
                        charts["necessities_cpi_vs_income"],
                    )
                ],
            ),
            # Monthly Expenditure
            create_section_title("Monthly Expenditure Breakdown"),
            create_card_graph(
                title="Breakdown of Monthly Expenditure Over Time",
                short_desc=MONTHLY_EXPENDITURE_Short,
                full_desc=MONTHLY_EXPENDITURE,
                graphs=[
                    (
                        "monthly_expenditure_donut_chart",
                        charts["monthly_expenditure_donut"],
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
                            className="text-2xl font-bold text-palette3",
                        ),
                        dmc.Divider(
                            className="my-2", color="var(--palette3)", size="sm"
                        ),
                        dmc.Text(
                            NECESSITIES_RECO,
                            className="text-base font-normal leading-relaxed",
                        ),
                    ],
                    className="p-6",
                ),
                shadow="sm",
                radius="lg",
                className="bg-white transition-all duration-300 hover:shadow-xl mt-2 mb-12 w-full",
                withBorder=True,
                style={"borderColor": "var(--palette3)", "borderWidth": "2px"},
            ),
        ],
        className="p-8 w-full",
        gap="md",
    )

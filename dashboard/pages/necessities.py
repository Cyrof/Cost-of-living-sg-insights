import dash
import dash_mantine_components as dmc
from dash.development.base_component import Component
from plotly.graph_objects import Figure
from text.necessitiesText import *

import dashboard.utils
from dashboard.components.textComponents import (create_card_graph,
                                                 create_page_title,
                                                 create_section_title)

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_necessities_charts()

    return dmc.Stack(
        className="w-full",
        gap="md",
        children=[
            # Header
            create_page_title(
                "Necessities Dashboard",
                "Analysing essential expenses and economic indicators",
            ),
            create_section_title("What are the cost of living trends?"),
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
            dmc.Divider(),
            # cpi vs income
            create_section_title("How do our incomes measure against our expenses?"),
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
            dmc.Divider(),
            # Monthly Expenditure
            create_section_title("How are Singaporeans spending their money?"),
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
            dmc.Divider(),
            # recommendation
            create_section_title("Our Recommendations"),
            dmc.Text(
                NECESSITIES_RECO,
                className="text-base font-normal leading-relaxed",
            ),
        ],
    )

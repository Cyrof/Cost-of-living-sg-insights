import dash
import dash_mantine_components as dmc
from dash.development.base_component import Component
from plotly.graph_objects import Figure

import dashboard.utils
from dashboard.components.textComponents import (create_card_graph,
                                                 create_page_title,
                                                 create_section_title)
from dashboard.text.necessitiesText import *

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_necessities_charts()

    return dmc.Stack(
        className="w-full",
        gap="md",
        children=[
            # Header
            create_page_title(
                "Necessities",
                "Analysing essential expenses and economic indicators",
            ),
            create_section_title("What are the cost of living trends?"),
            create_card_graph(
                title="Breakdown of Necessities CPI Over Time",
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(NECESSITIES_CPI_SHORT_1),
                                dmc.ListItem(NECESSITIES_CPI_SHORT_2),
                                dmc.ListItem(NECESSITIES_CPI_SHORT_3),
                                dmc.ListItem(NECESSITIES_CPI_SHORT_4),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(NECESSITIES_CPI_1),
                        dmc.Text(NECESSITIES_CPI_2),
                    ]
                ),
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
                title="CPI of Necessities Against Gross Monthly Income",
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(CPI_AGAINST_INCOME_SHORT_1),
                                dmc.ListItem(CPI_AGAINST_INCOME_SHORT_2),
                                dmc.ListItem(CPI_AGAINST_INCOME_SHORT_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(CPI_AGAINST_INCOME_1),
                        dmc.Text(CPI_AGAINST_INCOME_2),
                    ]
                ),
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
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(MONTHLY_EXPENDITURE_SHORT_1),
                                dmc.ListItem(MONTHLY_EXPENDITURE_SHORT_2),
                                dmc.ListItem(MONTHLY_EXPENDITURE_SHORT_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(MONTHLY_EXPENDITURE_1),
                        dmc.Text(MONTHLY_EXPENDITURE_2),
                    ]
                ),
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
            dmc.Text(NECESSITIES_RECO),
        ],
    )

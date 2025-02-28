import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure

import dashboard.utils

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

    return html.Div(
        [
            html.H1("Necessities"),
            dcc.Graph(
                id="necessities_cpi_breakdown_chart",
                figure=charts["necessities_cpi_breakdown"],
            ),
            dcc.Graph(
                id="necessities_cpi_vs_income_chart",
                figure=charts["necessities_cpi_vs_income"],
            ),
            dcc.Graph(
                id="monthly_expenditure_donut_chart",
                figure=charts["monthly_expenditure_donut"],
            ),
        ]
    )

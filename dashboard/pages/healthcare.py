import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure

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

    return html.Div(
        [
            html.H1("Healthcare"),
            dcc.Graph(
                id="life_expectancy_vs_healthcare_cpi_chart",
                figure=charts["life_expectancy_vs_healthcare_cpi"],
            ),
            dcc.Graph(
                id="healthcare_cpi_vs_gross_monthly_income_chart",
                figure=charts["healthcare_cpi_vs_gross_monthly_income"],
            ),
            dcc.Graph(
                id="percentage_change_in_healthcare_cpi_and_income_chart",
                figure=charts["percentage_change_in_healthcare_cpi_and_income"],
            ),
            dcc.Graph(
                id="healthcare_cpi_breakdown_chart",
                figure=charts["healthcare_cpi_breakdown"],
            ),
        ]
    )

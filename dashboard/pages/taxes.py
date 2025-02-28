import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure

import dashboard.utils

dash.register_page(__name__)


def load_charts() -> dict[str, Figure]:
    return {
        "iras_tax_collection_bar": dashboard.utils.load_chart_json(
            "iras_tax_collection_bar.json"
        ),
        "cpi_vs_gst_line_bar": dashboard.utils.load_chart_json(
            "cpi_vs_gst_line_bar.json"
        ),
        "income_tax_rates_step_line": dashboard.utils.load_chart_json(
            "income_tax_rates_step_line.json"
        ),
        "income_tax_heatmap": dashboard.utils.load_chart_json(
            "income_tax_heatmap.json"
        ),
        "property_tax_rates_step_line": dashboard.utils.load_chart_json(
            "property_tax_rates_step_line.json"
        ),
        "property_tax_collection_annual_value_bubble": (
            dashboard.utils.load_chart_json(
                "property_tax_collection_annual_value_bubble.json"
            )
        ),
    }


def layout() -> Component:
    charts: dict[str, Figure] = load_charts()
    return html.Div(
        [
            html.H1("Taxes"),
            dcc.Graph(
                id="iras_tax_collcetion_bar",
                figure=charts["iras_tax_collection_bar"],
            ),
            dcc.Graph(
                id="cpi_vs_gst_line_bar",
                figure=charts["cpi_vs_gst_line_bar"],
            ),
            dcc.Graph(
                id="income_tax_rates_step_line",
                figure=charts["income_tax_rates_step_line"],
            ),
            dcc.Graph(
                id="income_tax_heatmap",
                figure=charts["income_tax_heatmap"],
            ),
            dcc.Graph(
                id="property_tax_rates_step_line",
                figure=charts["property_tax_rates_step_line"],
            ),
            dcc.Graph(
                id="property_tax_collection_annual_value_bubble",
                figure=charts["property_tax_collection_annual_value_bubble"],
            ),
        ]
    )

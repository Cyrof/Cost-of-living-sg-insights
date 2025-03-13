import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc

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
    return dmc.Stack(
        [
            dmc.Stack(
                [
                    dmc.Text(
                        "GST",
                        className="text-3xl font-semibold"
                    ),
                    dmc.SimpleGrid(
                        cols=2,
                        spacing="lg",
                        children=[
                            dmc.Text(
                                "cpi against gst text",
                                className="border border-red-500"
                            ),
                            dmc.Text(
                                "tax collected by IRAS text",
                                className="border border-blue-500"
                            ),
                            dmc.Box(
                                [
                                    dcc.Graph(
                                        id="cpi_vs_gst_line_bar",
                                        figure=charts["cpi_vs_gst_line_bar"],
                                        className="w-[90%] h-auto"
                                    ),
                                ],
                                className="rounded-xl shadow-xl flex justify-center bg-white"
                            ),
                            dmc.Box(
                                [
                                    dcc.Graph(
                                        id="iras_tax_collection_bar",
                                        figure=charts["iras_tax_collection_bar"],
                                        className="w-[90%] h-auto"
                                    ),
                                ],
                                className="rounded-xl shadow-xl flex justify-center bg-white"
                            ),
                        ]
                    )
                ]
            ),
            dmc.Stack(
                [
                    dmc.Text(
                        "Income Tax",
                        className="text-3xl font-semibold"
                    ),
                    dmc.Group(
                        gap="lg",
                        grow=True,
                        children=[
                            dmc.Text(
                                "Income Tax Rates by Yearly Income Ranges text",
                                className="border border-purple-500"
                            ),
                            dmc.Box(
                                [
                                    dcc.Graph(
                                        id="income_tax_rates_step_line",
                                        figure=charts["income_tax_rates_step_line"],
                                        className="w-[90%] h-auto"
                                    ),
                                ],
                                className="rounded-xl shadow-xl flex justify-center bg-white"
                            )
                        ],
                    ),
                    dmc.Group(
                        gap="lg",
                        grow=True,
                        children=[
                            dmc.Box(
                                [
                                    dcc.Graph(
                                        id="income_tax_heatmap",
                                        figure=charts["income_tax_heatmap"],
                                        className="w-[90%] h-auto"
                                    ),
                                ],
                                className="rounded-xl shadow-xl flex justify-center bg-white"
                            ),

                            dmc.Text(
                                "Percentage of Assessed Income Paid in Taxes text",
                                className="border border-yellow-500"
                            )
                        ]
                    )
                ],
                className="mt-12"
            ),
            dmc.Stack(
                [
                    dmc.Text(
                        "Property Tax",
                        className="text-3xl font-semibold"
                    ),
                    dmc.Group(
                        gap="lg",
                        grow=True,
                        children=[
                            dmc.Text(
                                "Property Tax(Annual Value) some text here",
                                className="border border-green-500"
                            ),
                            dmc.Box(
                                [
                                    dcc.Graph(
                                        id="property_tax_rates_step_line",
                                        figure=charts["property_tax_rates_step_line"],
                                        className="w-[90%] h-auto",
                                        responsive=True
                                    ),
                                ],
                                className="rounded-xl shadow-xl flex justify-center bg-white"
                            ),
                        ]
                    ),
                    dmc.Group(
                        gap="lg",
                        grow=True,
                        children=[
                            dmc.Box(
                                 [
                                     dcc.Graph(
                                         id="property_tax_collection_annual_value_bubble",
                                         figure=charts["property_tax_collection_annual_value_bubble"],
                                         className="w-[90%] h-auto"
                                     ),
                                 ],
                                className="rounded-xl shadow-xl flex justify-center bg-white"
                            ),
                            dmc.Text(
                                "Property Tax (Annual Value by year & HDB Types) some text here",
                                className="border border-cyan-500"
                            )
                        ]
                    )
                ],
                className="mt-12"
            ),
        ],
        className="py-2 px-4"
    )
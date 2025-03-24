import dash
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper
from components.textComponents import create_card, create_section_title
from text.taxesText import *

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
            # header
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Text(
                            "Taxes Dashboard",
                            className="text-4xl font-extrabold text-palette4 text-center"
                        ),
                        dmc.Text(
                            "Tracking tax policies and financial impacts",
                            className="text-xl font-medium text-palette3 text-center opacity-80"
                        )
                    ],
                    gap="xs",
                    className="py-6"
                ),
                className="bg-palette1 rounded-xl mb-8 shadow-lg w-full",
                withBorder=False,
            ),
            # gst section
            create_section_title("Goods and Service Tax (GST) Overview"),
            dmc.SimpleGrid(
                cols=2,
                spacing="lg",
                children=[
                    create_card(
                        "CPI against GST",
                        CPI_AGAINST_GST,
                        "w-full"
                    ),
                    create_card(
                        "Tax Collected By IRAS",
                        TAX_COLLECTED_IRAS,
                        "w-full"
                    ),
                    dmc.Paper(
                        graphWrapper(
                            id="cpi_vs_gst_line_bar",
                            figure=charts["cpi_vs_gst_line_bar"]
                        ),
                        shadow="sm",
                        radius="lg",
                        className="w-full transition-all duration-300 hover:shadow-xl",
                        withBorder=True,
                        style={
                            "borderColor": "var(--palette3)",
                            "borderWidth": "2px"
                        }
                    ),
                    dmc.Paper(
                        graphWrapper(
                            id="iras_tax_collection_bar",
                            figure=charts["iras_tax_collection_bar"]
                        ),
                        shadow="sm",
                        radius="lg",
                        className="w-full transition-all duration-300 hover:shadow-xl",
                        withBorder=True,
                        style={
                            "borderColor": "var(--palette3)",
                            "borderWidth": "2px"
                        }
                    ),
                ],
            ),
            # income tax
            create_section_title("Income Tax Trends & Analysis"),
            dmc.Stack(
                [
                    dmc.Group(
                        gap="xl",
                        grow=True,
                        children=[
                            create_card(
                                "Income Tax Rates Step Line",
                                INCOME_TAX_STEP,
                                "w-1/2"
                            ),
                            dmc.Paper(
                                graphWrapper(
                                    id="income_tax_rates_step_line",
                                    figure=charts["income_tax_rates_step_line"]
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
                        ],
                        className="mt-2 h-[28rem] w-full"
                    ),
                    dmc.Group(
                        gap="xl",
                        grow=True,
                        children=[
                            dmc.Paper(
                                graphWrapper(
                                    id="income_tax_heatmap",
                                    figure=charts["income_tax_heatmap"]
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
                                "Percentage of Assessed Income Paid in Taxes",
                                INCOME_TAX_HEATMAP,
                                "w-1/2"
                            )
                        ],
                        className="mt-2 h-[28rem] w-full"
                    )
                ],
            ),
            # property tax
            create_section_title("Property Tax Insights"),
            dmc.Stack(
                [
                    dmc.Group(
                        gap="lg",
                        grow=True,
                        children=[
                            create_card(
                                "Property Tax (Annual Value)",
                                PROPERTY_TAX_ANNUAL,
                                "w-1/2"
                            ),
                            dmc.Paper(
                                graphWrapper(
                                    id="property_tax_rates_step_line",
                                    figure=charts["property_tax_rates_step_line"]
                                ),
                                shadow="sm",
                                radius="lg",
                                className="w-1/2 transition-all duration-300 hover:shadow-xl h-auto",
                                withBorder=True,
                                style={
                                    "borderColor": "var(--palette3)",
                                    "borderWidth": "2px"
                                }
                            )
                        ],
                        className="mt-2 h-[28rem] w-full"
                    ),
                    dmc.Group(
                        gap="lg",
                        grow=True,
                        children=[
                            dmc.Paper(
                                graphWrapper(
                                    id="property_tax_collection_annual_value_bubble",
                                    figure=charts["property_tax_collection_annual_value_bubble"]
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
                                "Property Tax (Annual Value by Year & HDB Types)",
                                PROPERTY_TAX_ANNUAL_HDB,
                                "w-1/2"
                            )
                        ],
                        className="mt-2 h-[28rem] w-full"
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
                            className="my-2",
                            color="var(--palette3)",
                            size="sm"
                        ),
                        dmc.Text(
                            TAX_RECO,
                            className="pl-6 text-base font-nnormal leading-relaxed text-palette3"
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
        gap="md"
    )
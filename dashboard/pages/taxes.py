import dash
import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper
from components.textComponents import (
    create_card,
    create_card_graph,
    create_section_title,
)
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure
from text.taxesText import *

import dashboard.utils

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_taxes_charts()
    return dmc.Stack(
        [
            # header
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Title(
                            "Taxes Dashboard",
                            className="text-4xl font-extrabold text-palette4 text-center",
                        ),
                        dmc.Title(
                            "Tracking tax policies and financial impacts",
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
            # gst section
            create_section_title("Goods and Service Tax (GST) Overview"),
            create_card_graph(
                title="CPI against GST",
                short_desc=CPI_AGAINST_GST_Short,
                full_desc=CPI_AGAINST_GST,
                graphs=[
                    (
                        "cpi_vs_gst_line_bar",
                        charts["cpi_vs_gst_line_bar"],
                    ),
                ],
            ),
            create_card_graph(
                title="Tax Collected By IRAS",
                short_desc=TAX_COLLECTED_IRAS_Short,
                full_desc=TAX_COLLECTED_IRAS,
                graphs=[
                    (
                        "iras_tax_collection_bar",
                        charts["iras_tax_collection_bar"],
                    )
                ],
            ),
            # income tax
            create_section_title("Income Tax Trends & Analysis"),
            create_card_graph(
                title="Income Tax Rates Step Line",
                short_desc=INCOME_TAX_STEP_Short,
                full_desc=INCOME_TAX_STEP,
                graphs=[
                    ("income_tax_rates_step_line", charts["income_tax_rates_step_line"])
                ],
            ),
            create_card_graph(
                title="Percentage of Assessed Income Paid in Taxes",
                short_desc=INCOME_TAX_HEATMAP_Short,
                full_desc=INCOME_TAX_HEATMAP,
                graphs=[("income_tax_heatmap", charts["income_tax_heatmap"])],
            ),
            # property tax
            create_section_title("Property Tax Insights"),
            create_card_graph(
                title="Property Tax (Annual Value)",
                short_desc=PROPERTY_TAX_ANNUAL_Short,
                full_desc=PROPERTY_TAX_ANNUAL,
                graphs=[
                    (
                        "property_tax_rates_step_line",
                        charts["property_tax_rates_step_line"],
                    )
                ],
            ),
            create_card_graph(
                title="Property Tax (Annual Value by Year & HDB Types)",
                short_desc=PROPERTY_TAX_ANNUAL_HDB_Short,
                full_desc=PROPERTY_TAX_ANNUAL_HDB,
                graphs=[
                    (
                        "property_tax_collection_annual_value_bubble",
                        charts["property_tax_collection_annual_value_bubble"],
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
                            TAX_RECO,
                            className="text-base font-nnormal leading-relaxed text-palette3",
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

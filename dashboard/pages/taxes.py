import dash
import dash_mantine_components as dmc
from dash.development.base_component import Component
from plotly.graph_objects import Figure
from text.taxesText import *

import dashboard.utils
from dashboard.components.textComponents import (create_card_graph,
                                                 create_page_title)

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_taxes_charts()
    return dmc.Stack(
        className="w-full",
        gap="md",
        children=[
            # header
            create_page_title(
                "Taxes",
                "Analysing tax policies and financial impacts",
            ),
            # overview
            dmc.Title("How much tax does the IRAS collect?", order=2),
            create_card_graph(
                title="Tax Collected by the IRAS",
                short_desc=TAX_COLLECTED_IRAS_Short,
                full_desc=TAX_COLLECTED_IRAS,
                graphs=[
                    (
                        "iras_tax_collection_bar",
                        charts["iras_tax_collection_bar"],
                    )
                ],
            ),
            dmc.Divider(),
            # gst section
            dmc.Title("How does the goods and service tax (GST) affect CPI?", order=2),
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
            dmc.Divider(),
            # income tax
            dmc.Title("What are the income tax trends?", order=2),
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
            dmc.Divider(),
            # property tax
            dmc.Title("What are the property tax trends?", order=2),
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
            dmc.Divider(),
            # recommendation
            dmc.Title("Our Recommendations", order=2),
            dmc.Text(TAX_RECO),
        ],
    )

import dash
import dash_mantine_components as dmc
from dash.development.base_component import Component
from plotly.graph_objects import Figure

import dashboard.utils
from dashboard.components.textComponents import (create_card_graph,
                                                 create_data_sources,
                                                 create_page_title)
from dashboard.text.taxesText import *

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
                sources=create_data_sources(
                    [
                        (
                            "IRAS' Collection by Tax Type",
                            "https://data.gov.sg/datasets/d_21e22578cabce897e8b27801e5596140/view",
                        )
                    ]
                ),
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(TAX_COLLECTED_IRAS_SHORT_BULLET_1),
                                dmc.ListItem(TAX_COLLECTED_IRAS_SHORT_BULLET_2),
                                dmc.ListItem(TAX_COLLECTED_IRAS_SHORT_BULLET_3),
                                dmc.ListItem(TAX_COLLECTED_IRAS_SHORT_BULLET_4),
                            ]
                        ),
                    ],
                ),
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
            dmc.Title("How does GST correlate with CPI?", order=2),
            create_card_graph(
                title="CPI against GST",
                sources=create_data_sources(
                    [
                        (
                            "Consumer Price Index (CPI), 2019 As Base Year, Annual",
                            "https://data.gov.sg/datasets/d_dcb352661fb449c4a4c0ab23aa8d6399/view",
                        ),
                        (
                            "Tax Rates for Goods and Services Tax",
                            "https://data.gov.sg/datasets/d_2e65ed309aa8d449d1bd0c7ef7c7e4da/view",
                        ),
                    ]
                ),
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(CPI_VS_GST_SHORT_BULLET_1),
                                dmc.ListItem(CPI_VS_GST_SHORT_BULLET_2),
                                dmc.ListItem(CPI_VS_GST_SHORT_BULLET_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    children=[
                        dmc.Text(CPI_VS_GST_1),
                        dmc.Text(CPI_VS_GST_2),
                    ]
                ),
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
                sources=create_data_sources(
                    [
                        (
                            "Tax Rates for Individual Income Tax",
                            "https://data.gov.sg/datasets/d_f73055c69144d2e7734c28811d3982aa/view",
                        )
                    ]
                ),
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(INCOME_TAX_STEP_SHORT_BULLET_1),
                                dmc.ListItem(INCOME_TAX_STEP_SHORT_BULLET_2),
                                dmc.ListItem(INCOME_TAX_STEP_SHORT_BULLET_3),
                                dmc.ListItem(INCOME_TAX_STEP_SHORT_BULLET_4),
                            ]
                        ),
                    ],
                ),
                full_desc=INCOME_TAX_STEP,
                graphs=[
                    ("income_tax_rates_step_line", charts["income_tax_rates_step_line"])
                ],
            ),
            create_card_graph(
                title="Percentage of Assessed Income Paid in Taxes",
                sources=create_data_sources(
                    [
                        (
                            "Taxable Individuals by Assessed Income Group",
                            "https://data.gov.sg/datasets/d_f394f202534237671d39b17bd3b506ec/view",
                        )
                    ]
                ),
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(INCOME_TAX_HEATMAP_SHORT_BULLET_1),
                                dmc.ListItem(INCOME_TAX_HEATMAP_SHORT_BULLET_2),
                                dmc.ListItem(INCOME_TAX_HEATMAP_SHORT_BULLET_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    children=[
                        dmc.Text(INCOME_TAX_HEATMAP_1),
                        dmc.Text(INCOME_TAX_HEATMAP_2),
                    ]
                ),
                graphs=[("income_tax_heatmap", charts["income_tax_heatmap"])],
            ),
            dmc.Divider(),
            # property tax
            dmc.Title("What are the property tax trends?", order=2),
            create_card_graph(
                title="Property Tax (Annual Value)",
                sources=create_data_sources(
                    [
                        (
                            "Tax Rates for Property Tax",
                            "https://data.gov.sg/datasets/d_2109ad1eafff52dab388f9bcd8148a35/view",
                        )
                    ]
                ),
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(PROPERTY_TAX_ANNUAL_SHORT_BULLET_1),
                                dmc.ListItem(PROPERTY_TAX_ANNUAL_SHORT_BULLET_2),
                                dmc.ListItem(PROPERTY_TAX_ANNUAL_SHORT_BULLET_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    children=[
                        dmc.Text(PROPERTY_TAX_ANNUAL_1),
                        dmc.Text(PROPERTY_TAX_ANNUAL_2),
                    ]
                ),
                graphs=[
                    (
                        "property_tax_rates_step_line",
                        charts["property_tax_rates_step_line"],
                    )
                ],
            ),
            create_card_graph(
                title="Property Tax (Annual Value by Year & HDB Types)",
                sources=create_data_sources(
                    [
                        (
                            "Median Annual Value and Property Tax By Type of HDB",
                            "https://data.gov.sg/datasets/d_48143be392f1ed22f0700835212e5a60/view",
                        )
                    ]
                ),
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(PROPERTY_TAX_ANNUAL_HDB_SHORT_BULLET_1),
                                dmc.ListItem(PROPERTY_TAX_ANNUAL_HDB_SHORT_BULLET_2),
                                dmc.ListItem(PROPERTY_TAX_ANNUAL_HDB_SHORT_BULLET_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    children=[
                        dmc.Text(PROPERTY_TAX_ANNUAL_HDB_1),
                        dmc.Text(PROPERTY_TAX_ANNUAL_HDB_2),
                    ]
                ),
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
            dmc.Title("GST", order=3),
            dmc.Text(TAX_RECO_GST),
            dmc.Title("Income Tax", order=3),
            dmc.Text(TAX_RECO_INCOME_TAX),
            dmc.Title("Property Tax", order=3),
            dmc.Text(TAX_RECO_PROPERTY_TAX),
        ],
    )

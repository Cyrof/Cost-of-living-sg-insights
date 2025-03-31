import dash
import dash_mantine_components as dmc
from dash.development.base_component import Component
from plotly.graph_objects import Figure
from text.healthcareText import *

import dashboard.utils
from dashboard.components.textComponents import (create_card_graph,
                                                 create_page_title,
                                                 create_section_title)

dash.register_page(__name__)


def layout() -> Component:
    charts: dict[str, Figure] = dashboard.utils.load_healthcare_charts()
    return dmc.Stack(
        className="w-full",
        gap="md",
        children=[
            # header
            create_page_title(
                "Healthcare",
                "Analysing healthcare costs and market dynamics",
            ),
            # healthcare breakdown
            create_section_title("Are the costs of healthcare services increasing?"),
            create_card_graph(
                title="Breakdown of Healthcare CPI",
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(HEALTHCARE_COM_SHORT_1),
                                dmc.ListItem(HEALTHCARE_COM_SHORT_2),
                                dmc.ListItem(HEALTHCARE_COM_SHORT_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(HEALTHCARE_COM_1),
                        dmc.Text(HEALTHCARE_COM_2),
                    ]
                ),
                graphs=[
                    (
                        "healthcare_cpi_breakdown_chart",
                        charts["healthcare_cpi_breakdown"],
                    )
                ],
            ),
            dmc.Divider(),
            # life expectancy vs healthcare & healthcare vs income
            create_section_title("How do healthcare costs compare with income?"),
            create_card_graph(
                title="Life Expectancy VS Healthcare CPI",
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(LIFE_EXPECTANCY_HEALTHCARE_SHORT_1),
                                dmc.ListItem(LIFE_EXPECTANCY_HEALTHCARE_SHORT_2),
                                dmc.ListItem(LIFE_EXPECTANCY_HEALTHCARE_SHORT_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(LIFE_EXPECTANCY_HEALTHCARE_1),
                        dmc.Text(LIFE_EXPECTANCY_HEALTHCARE_2),
                        dmc.Text(LIFE_EXPECTANCY_HEALTHCARE_3),
                    ]
                ),
                # figure=charts["life_expectancy_vs_healthcare_cpi"],
                # card_id="life_expectancy_vs_healthcare_cpi_chart",
                graphs=[
                    (
                        "life_expectancy_vs_healthcare_cpi_chart",
                        charts["life_expectancy_vs_healthcare_cpi"],
                    )
                ],
            ),
            create_card_graph(
                title="Healthcare CPI VS Income Growth",
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(HEALTHCARE_VS_INCOME_SHORT_1),
                                dmc.ListItem(HEALTHCARE_VS_INCOME_SHORT_2),
                                dmc.ListItem(HEALTHCARE_VS_INCOME_SHORT_3),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(HEALTHCARE_VS_INCOME_1),
                        dmc.Text(HEALTHCARE_VS_INCOME_2),
                        dmc.Text(HEALTHCARE_VS_INCOME_3),
                    ]
                ),
                graphs=[
                    (
                        "healthcare_cpi_vs_gross_monthly_income",
                        charts["healthcare_cpi_vs_gross_monthly_income"],
                    )
                ],
            ),
            create_card_graph(
                title="Healthcare CPI vs Income Growth (%)",
                short_desc=dmc.Stack(
                    children=[
                        dmc.Text("Summary:"),
                        dmc.List(
                            children=[
                                dmc.ListItem(HEALTHCARE_VS_INCOME_PERCENTAGE_SHORT_1),
                                dmc.ListItem(HEALTHCARE_VS_INCOME_PERCENTAGE_SHORT_2),
                            ]
                        ),
                    ],
                ),
                full_desc=dmc.Stack(
                    [
                        dmc.Text(HEALTHCARE_VS_INCOME_PERCENTAGE_1),
                        dmc.Text(HEALTHCARE_VS_INCOME_PERCENTAGE_2),
                    ]
                ),
                # figure=charts["percentage_change_in_healthcare_cpi_and_income"],
                # card_id="percentage_change_in_healthcare_cpi_and_income_chart",
                graphs=[
                    (
                        "percentage_change_in_healthcare_cpi_and_income_chart",
                        charts["percentage_change_in_healthcare_cpi_and_income"],
                    )
                ],
            ),
            dmc.Divider(),
            # recommendation
            create_section_title("Our Recommendations"),
            dmc.Stack(
                [
                    dmc.Text(HEALTHCARE_RECO_1),
                    dmc.Text(HEALTHCARE_RECO_2),
                ]
            ),
        ],
    )

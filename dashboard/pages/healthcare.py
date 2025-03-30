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
                short_desc=HEALTHCARE_COM_Short,
                full_desc=HEALTHCARE_COM,
                # figure=charts["healthcare_cpi_breakdown"],
                # card_id="healthcare_cpi_breakdown_chart"
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
                short_desc=LIFE_EXPECTANCY_HEALTHCARE_Short,
                full_desc=LIFE_EXPECTANCY_HEALTHCARE,
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
                short_desc=HEALTHCARE_VS_INCOME_Short,
                full_desc=HEALTHCARE_VS_INCOME,
                graphs=[
                    (
                        "healthcare_cpi_vs_gross_monthly_income",
                        charts["healthcare_cpi_vs_gross_monthly_income"],
                    )
                ],
            ),
            create_card_graph(
                title="Healthcare CPI vs Income Growth (%)",
                short_desc=HEALTHCARE_VS_INCOME_PERCENTAGE_Short,
                full_desc=HEALTHCARE_VS_INCOME_PERCENTAGE,
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
            dmc.Text(
                HEALTHCARE_RECO,
            ),
        ],
    )

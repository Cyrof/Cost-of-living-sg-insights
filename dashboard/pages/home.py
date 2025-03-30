import dash
import dash_mantine_components as dmc
from plotly.graph_objects import Figure
from text.home_text import *

import dashboard.utils
from dashboard.components.hoverCard import hoverableCard
from dashboard.components.textComponents import create_section_title

dash.register_page(__name__, path="/")


def layout():
    charts: dict[str, Figure] = dashboard.utils.load_home_charts()

    return dmc.Stack(
        children=[
            create_section_title(HYPO_QNS),
            dmc.Title(
                "Introduction",
                order=2,
            ),
            dmc.Group(
                className="w-full",
                grow=True,
                gap="xl",
                preventGrowOverflow=True,
                align="flex-start",
                children=[
                    # left panel text
                    dmc.Stack(
                        children=[
                            dmc.Text(INTRO_1),
                            dmc.Text(INTRO_2),
                        ],
                    ),
                    # right panel text
                    dmc.Stack(
                        children=[
                            dmc.Text("Specifically, we hypothesize that:"),
                            dmc.List(
                                listStyleType="disc",
                                children=[
                                    dmc.ListItem(INTRO_BULLET_1),
                                    dmc.ListItem(INTRO_BULLET_2),
                                    dmc.ListItem(INTRO_BULLET_3),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            dmc.Text(INTRO_3),
            create_section_title("Explore Insights"),
            dmc.Box(
                [
                    dmc.SimpleGrid(
                        cols=2,
                        spacing="md",
                        children=[
                            hoverableCard(
                                chartID="iras_tax_collection_bar",
                                chart=charts["iras_tax_collection_bar"],
                                cardName="Taxes",
                                desc="Is Singapore's tax system effective? How does it affect different income levels and property values?",
                                href="/taxes",
                            ),
                            hoverableCard(
                                chartID="necessities_cpi_vs_income",
                                chart=charts["necessities_cpi_vs_income"],
                                cardName="Necessities",
                                desc="Are the costs of essential goods and services, such as housing, food, healthcare and transportation, become less affordable?",
                                href="/necessities",
                            ),
                            hoverableCard(
                                chartID="percentage_change_in_healthcare_cpi_and_income",
                                chart=charts[
                                    "percentage_change_in_healthcare_cpi_and_income"
                                ],
                                cardName="Healthcare",
                                desc="Are healthcare costs rising and impacting affordability and access?",
                                href="/healthcare",
                            ),
                            hoverableCard(
                                chartID="cpi_bubble_map",
                                chart=charts["cpi_bubble_map"],
                                cardName="Global",
                                desc="How does Singapore's economic situation compare with other countries?",
                                href="/global",
                            ),
                        ],
                        className="my-6",
                    )
                ],
            ),
            create_section_title("Our Final Thoughts"),
            dmc.Stack(
                [
                    dmc.Text(CONCLUSION_1),
                    dmc.Text(CONCLUSION_2),
                    dmc.Text(CONCLUSION_3),
                    dmc.Text(CONCLUSION_4),
                ],
            ),
        ],
    )

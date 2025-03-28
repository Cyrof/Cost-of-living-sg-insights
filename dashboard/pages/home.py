import dash
import plotly.express as px
from dash import dcc, html
import dash_mantine_components as dmc
from components.hoverCard import hoverableCard
from plotly.graph_objects import Figure
import dashboard.utils
from text.home_text import *
from components.textComponents import create_card, create_section_title

dash.register_page(__name__, path="/")


def layout():
    charts: dict[str, Figure] = dashboard.utils.load_home_charts()

    return dmc.Stack(
        children=[
            create_section_title(HYPO_QNS),
            dmc.Group(
                [
                    # left panel text
                    dmc.Box(
                        [
                            dmc.Text(
                                "Introduction", className="text-xl font-semibold text-palette4 mb-4"),
                            dmc.Text([INTRO_1, INTRO_2],
                                     className="text-lg text-palette4")
                        ],
                        className="h-full"
                    ),
                    # right panel text
                    dmc.Box(
                        [
                            dmc.Text("Specifically, we hypothesize that:",
                                     className="text-xl font-semibold text-palette4 mb-4"),
                            dmc.List(
                                [
                                    dmc.ListItem(INTRO_BULLET_1),
                                    dmc.ListItem(INTRO_BULLET_2),
                                    dmc.ListItem(INTRO_BULLET_3),
                                ],
                                className="list-disc text-lg text-palette4"
                            )
                        ],
                        className="h-full"
                    )
                ],
                className="w-full",
                grow=True,
                preventGrowOverflow=True,
                align="flex-start",
            ),

            dmc.Text(INTRO_3, className="text-lg text-palette4"),
            create_section_title("Explore Key Insights"),
            dmc.Box(
                [
                    dmc.SimpleGrid(
                        cols=2,
                        spacing="sm",
                        children=[
                            hoverableCard(
                                chartID="percentage_change_in_healthcare_cpi_and_income",
                                chart=charts["percentage_change_in_healthcare_cpi_and_income"],
                                cardName="Healthcare",
                                desc="Short description for healthcare",
                                href="/healthcare"
                            ),
                            hoverableCard(
                                chartID="cpi_vs_gst_line_bar",
                                chart=charts["cpi_vs_gst_line_bar"],
                                cardName="Taxes",
                                desc="Short description for taxes",
                                href="/taxes"
                            ),
                            hoverableCard(
                                chartID="necessities_cpi_vs_income",
                                chart=charts["necessities_cpi_vs_income"],
                                cardName="Necessities",
                                desc="Short description for necessities",
                                href="/necessities"
                            ),
                            hoverableCard(
                                chartID="cpi_bubble_map",
                                chart=charts["cpi_bubble_map"],
                                cardName="Global",
                                desc="Short description for global",
                                href="/global"
                            )
                        ],
                        className="my-6"
                    )
                ],
            ),
            create_section_title("Our Final Thoughts"),
            dmc.Stack(
                [
                    dmc.Text(CONCLUSION_1,
                             className="text-lg text-palette4"),
                    dmc.Text(CONCLUSION_2,
                             className="text-lg text-palette4"),
                    dmc.Text(CONCLUSION_3,
                             className="text-lg text-palette4"),
                    dmc.Text(CONCLUSION_4,
                             className="text-lg text-palette4"),
                ],
                className="px-6"
            ),
        ],
        className="pb-12"
    )

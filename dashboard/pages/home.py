import dash
import plotly.express as px
from dash import dcc, html
import dash_mantine_components as dmc
from components.hoverCard import hoverableCard
from plotly.graph_objects import Figure
import dashboard.utils
from text.home_text import *

dash.register_page(__name__, path="/")


def load_charts() -> dict[str, Figure]:
    return {
        "percentage_change_in_healthcare_cpi_and_income": dashboard.utils.load_chart_json(
            "percentage_change_in_healthcare_cpi_and_income.json"
        ),
        "cpi_vs_gst_line_bar": dashboard.utils.load_chart_json(
            "cpi_vs_gst_line_bar.json"
        ),
        "necessities_cpi_vs_income": dashboard.utils.load_chart_json(
            "necessities_cpi_vs_income.json"
        ),
        "cpi_bubble_map": dashboard.utils.load_chart_json("cpi_bubble_map.json"),
    }


def layout():
    charts: dict[str, Figure] = load_charts()

    return dmc.Stack(
        children=[
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Group(
                            [dmc.Text(
                                HYPO_QNS, className="text-3xl font-semibold text-palette3")],
                            justify="center",
                            className="w-full"
                        ),
                        dmc.Divider(className="my-2 bg-palette2"),
                        dmc.Stack(
                            [
                                dmc.Text([INTRO_1, INTRO_2],
                                         className="text-lg text-palette4"),
                                dmc.Text("Specifically, we hypothesize that:",
                                         className="text-lg font-semibold mt-4 text-palette3"),
                                dmc.List(
                                    [
                                        dmc.ListItem(INTRO_BULLET_1),
                                        dmc.ListItem(INTRO_BULLET_2),
                                        dmc.ListItem(INTRO_BULLET_3),
                                    ],
                                    className="list-disc ml-8 text-lg text-palette4"
                                ),
                                dmc.Text(
                                    INTRO_3, className="text-lg mt-4 text-palette4")
                            ],
                            gap="sm"
                        ),
                    ],
                    className="p-6"
                ),
                shadow="sm",
                radius="md",
                className="mb-8 bg-palette1",
                withBorder=True,
                style={"borderColor": "var(--palette3)"}
            ),
            dmc.Box(
                [
                    dmc.Text("Explore Key Insights",
                             className="text-2xl font-semibold mb-4 text-palette3"),
                    dmc.SimpleGrid(
                        cols=4,
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
                className="mb-8"
            ),
            dmc.Paper(
                dmc.Stack(
                    [
                        dmc.Text(
                            "Conclusion", className="text-3xl font-semibold text-palette3"),
                        dmc.Divider(className="my-2 bg-palette2"),
                        dmc.Text(CONCLUSION_1,
                                 className="text-lg text-palette4"),
                        dmc.Text(CONCLUSION_2,
                                 className="text-lg mt-2 text-palette4"),
                        dmc.Text(CONCLUSION_3,
                                 className="text-lg mt-2 text-palette4"),
                        dmc.Text(CONCLUSION_4,
                                 className="text-lg mt-2 text-palette4"),
                    ],
                    className="p-6"
                ),
                shadow="sm",
                radius="md",
                className="mb-8 bg-palette1",
                withBorder=True,
                style={"borderColor": "var(--palette3)"}
            )
        ],
        className="pb-12"
    )

import dash
import dash_mantine_components as dmc

from dashboard.components.hoverCard import hoverableCard
from dashboard.components.textComponents import (create_card,
                                                 create_page_title,
                                                 create_section_title)
from dashboard.text.home_text import *

dash.register_page(__name__, path="/")


def layout():
    # left panel text
    intro_para_1 = dmc.Stack(
        children=[
            dmc.Text(INTRO_1),
            dmc.Text(INTRO_2),
        ],
    )

    # right panel text
    intro_para_2 = dmc.Stack(
        children=[
            dmc.Text(INTRO_BULLET_HEADING),
            dmc.List(
                children=[
                    dmc.ListItem(INTRO_BULLET_1),
                    dmc.ListItem(INTRO_BULLET_2),
                    dmc.ListItem(INTRO_BULLET_3),
                    dmc.ListItem(INTRO_BULLET_4),
                ],
            ),
        ],
    )

    intro_para_3 = dmc.Text(INTRO_3)

    term_cards = [
        create_card(
            "Good Service Tax (GST)",
            GST_DEF,
            stackGap=0,
            dividerKwargs={"size": "sm"},
        ),
        create_card(
            "Gross Domestic Product (GDP) per Capita",
            GDP_DEF,
            stackGap=0,
            dividerKwargs={"size": "sm"},
        ),
        create_card(
            "Consumer Price Index (CPI)",
            CPI_DEF,
            stackGap=0,
            dividerKwargs={"size": "sm"},
        ),
        create_card(
            "Purchasing Power Parity (PPP)",
            PPP_DEF,
            stackGap=0,
            dividerKwargs={"size": "sm"},
        ),
    ]

    preview_cards = [
        hoverableCard(
            chartID="iras_tax_collection_bar",
            image_src=dash.get_asset_url("images/tax_preview.png"),
            cardName="Taxes",
            desc="Is Singapore's tax system effective? How does it affect different income levels and property values?",
            href="/taxes",
        ),
        hoverableCard(
            chartID="necessities_cpi_vs_income",
            image_src=dash.get_asset_url("images/necessities_preview.png"),
            cardName="Necessities",
            desc="Are the costs of essential goods and services, such as housing, food, healthcare and transportation, becoming less affordable?",
            href="/necessities",
        ),
        hoverableCard(
            chartID="percentage_change_in_healthcare_cpi_and_income",
            image_src=dash.get_asset_url("images/healthcare_preview.png"),
            cardName="Healthcare",
            desc="Are healthcare costs rising and impacting affordability and access?",
            href="/healthcare",
        ),
        hoverableCard(
            chartID="cpi_bubble_map",
            image_src=dash.get_asset_url("images/global_preview.png"),
            cardName="Global",
            desc="How does Singapore's economic situation compare to other countries?",
            href="/global",
        ),
    ]

    return dmc.Stack(
        children=[
            create_page_title(HYPO_QNS),
            create_section_title("Introduction"),
            dmc.Group(
                className="w-full",
                grow=True,
                gap="xl",
                preventGrowOverflow=True,
                align="flex-start",
                visibleFrom="sm",
                children=[
                    intro_para_1,
                    intro_para_2,
                ],
            ),
            dmc.Stack(
                hiddenFrom="sm",
                children=[
                    intro_para_1,
                    intro_para_2,
                ],
            ),
            intro_para_3,
            dmc.Divider(),
            create_section_title("Terminology"),
            dmc.Text(TERMINOLOGY_INTRO),
            dmc.Box(
                children=[
                    dmc.SimpleGrid(
                        cols=2,
                        spacing="md",
                        visibleFrom="sm",
                        children=term_cards,
                        className="my-6",
                    ),
                    dmc.Stack(
                        gap="md",
                        hiddenFrom="sm",
                        children=term_cards,
                        className="my-6",
                    ),
                ],
            ),
            dmc.Divider(),
            create_section_title("Explore Insights"),
            dmc.Box(
                [
                    dmc.SimpleGrid(
                        cols=2,
                        spacing="md",
                        visibleFrom="sm",
                        children=preview_cards,
                        className="my-6",
                    ),
                    dmc.Stack(
                        gap="xl",
                        hiddenFrom="sm",
                        children=preview_cards,
                        className="my-6",
                    ),
                ],
            ),
            dmc.Divider(),
            create_section_title("Our Final Thoughts"),
            dmc.Stack(
                [
                    dmc.Text(CONCLUSION_BULLET_HEADING),
                    dmc.List(
                        children=[
                            dmc.ListItem(CONCLUSION_BULLET_1),
                            dmc.ListItem(CONCLUSION_BULLET_2),
                            dmc.ListItem(CONCLUSION_BULLET_3),
                            dmc.ListItem(CONCLUSION_BULLET_4),
                        ],
                    ),
                    dmc.Text(CONCLUSION_CLOSING_1),
                    dmc.Text(CONCLUSION_CLOSING_2),
                ],
            ),
        ],
    )

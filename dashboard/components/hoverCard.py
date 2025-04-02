import base64

import cachetools
import dash_mantine_components as dmc
import plotly.io as pio
from cachetools.keys import hashkey
from dash import dcc, html
from plotly.graph_objects import Figure


# Cache using the chartID as the key.
@cachetools.cached(
    cache={}, key=lambda chartID, fig, img_format="png": hashkey(chartID)
)
def fig_to_base64(chartID: str, fig: Figure, img_format: str = "png") -> str:
    img_bytes = pio.to_image(fig, format=img_format)
    encoded = base64.b64encode(img_bytes).decode("ascii")
    return f"data:image/{img_format};base64,{encoded}"


def hoverableCard(
    chartID: str,
    image_src: str,
    cardName: str,
    desc: str,
    href: str,
) -> dmc.Card:
    return dmc.Box(
        className="group w-full",
        children=[
            dmc.Paper(
                p=30,
                h="auto",
                radius="md",
                className=(
                    "border transition-all duration-300 "
                    "transform group-hover:scale-105 shadow-xl"
                ),
                children=dmc.Stack(
                    gap="xs",
                    children=[
                        # card image
                        dmc.Stack(
                            p=0,
                            h=300,
                            justify="center",
                            children=html.Img(
                                className="h-auto w-full object-contain",
                                src=image_src,
                            ),
                        ),
                        # card title
                        dmc.Title(
                            cardName,
                            order=4,
                            ta="center",
                        ),
                        # On-hover context
                        dmc.Stack(
                            gap="md",
                            className=(
                                "transition-all duration-300 opacity-0 max-h-0 overflow-hidden "
                                "group-hover:opacity-100 group-hover:max-h-[200px]"
                            ),
                            children=[
                                dmc.Text(desc),
                                dmc.Group(
                                    dcc.Link(dmc.Button("Explore More"), href=href),
                                    justify="center",
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ],
    )

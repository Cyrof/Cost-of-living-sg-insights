import base64
import cachetools
from cachetools.keys import hashkey

import dash_mantine_components as dmc
import plotly.io as pio
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
    chartID: str, chart: Figure, cardName: str, desc: str, href: str
) -> dmc.Card:
    # conver to based64 image
    img_data = fig_to_base64(chartID, chart)

    return html.Div(
        className="group w-full",
        children=[
            dmc.Card(
                children=[
                    # card image
                    dmc.CardSection(
                        html.Img(src=img_data, className="w-auto h-60 block mx-auto "),
                    ),
                    # card title
                    dmc.Group(
                        children=[
                            dmc.Text(
                                cardName, className="text-xl font-semibold text-center"
                            )
                        ],
                        className="justify-center",
                    ),
                    # on hover context1
                    html.Div(
                        children=[
                            dmc.Text(desc),
                            dcc.Link(dmc.Button("Explore More"), href=href),
                        ],
                        className=(
                            "transition-all duration-300 opacity-0 max-h-0 overflow-hidden p-4 text-center "
                            "group-hover:opacity-100 group-hover:max-h-[200px]"
                        ),
                    ),
                ],
                className=(
                    "border rounded-xl overflow-hidden transition-all duration-300 p-4 m-4 w-full h-auto mx-auto "
                    "transform group-hover:scale-105 shadow-xl"
                ),
            )
        ],
    )

import os

os.environ["REACT_VERSION"] = "18.2.0"

import dash
from components.sidebar import sidebar
from components.topBar import topbar
from components.footer import footer
from dash import Dash, dcc, html
import dash_mantine_components as dmc
import dashboard.utils

FA = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"
TW = "https://cdn.tailwindcss.com"


def init_app():
    app = Dash(
        __name__,
        use_pages=True,
        pages_folder="pages",
        suppress_callback_exceptions=True,
        external_stylesheets=[FA] + dmc.styles.ALL,
        external_scripts=[TW],
    )

    app.layout = dmc.MantineProvider(
        forceColorScheme="dark",
        theme={
            "components": {
                "Text": {
                    "defaultProps": {
                        "ta": "justify",
                    },
                },
                "ListItem": {
                    "defaultProps": {
                        "ta": "justify",
                    },
                },
            },
        },
        children=[
            # dcc.location to tracks the current url
            dcc.Location(id="url", refresh=False),
            html.Div(
                className="min-h-screen flex flex-col",
                children=[
                    html.Header(
                        className="flex-none h-16",
                        children=[
                            topbar(),
                            sidebar(),
                        ],
                    ),
                    html.Main(
                        children=[
                            # page container
                            dmc.Group(
                                dmc.Box(
                                    dash.page_container,
                                    w=1000,
                                ),
                                className="py-8 px-20",
                                align="center",
                                justify="center",
                                bg="dark.8",  # Use Mantine theme color for background
                            ),
                        ],
                    ),
                    html.Footer(
                        children=[
                            footer(),
                        ]
                    ),
                ],
            ),
        ],
    )

    with app.server.app_context():
        dashboard.utils.warmup_cache()

    return app


app = init_app()


def main():
    app.run(debug=True, dev_tools_hot_reload=True)

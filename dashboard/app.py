import os
os.environ["REACT_VERSION"] = "18.2.0"

import dash
from components.sidebar import sidebar
from components.topBar import topbar
from dash import Dash, dcc, html
import dash_mantine_components as dmc

FA = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"
TW = "https://cdn.tailwindcss.com"

app = Dash(
    __name__, 
    use_pages=True, 
    pages_folder="pages", 
    suppress_callback_exceptions=True,
    external_stylesheets=[FA] + dmc.styles.ALL,
    external_scripts=[TW]
)

app.layout = dmc.MantineProvider(
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
                        # sidebar
                        sidebar(),
                    ]
                ),
                html.Main(
                    children=[
                        # page container
                        html.Div(dash.page_container, className="p-4 bg-palette1"),
                    ],
                ),
                ]
            ),
    ],
)


def main():
    app.run(debug=True, dev_tools_hot_reload=True)

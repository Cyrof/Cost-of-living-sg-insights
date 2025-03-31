import os

os.environ["REACT_VERSION"] = "18.2.0"

import dash_mantine_components as dmc
from dash import Dash

import dashboard.utils
from dashboard.components.app_shell import DashboardAppShell

FA = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"
TW = "https://cdn.tailwindcss.com"

# Add Mantine templates for styling Plotly figures.
dmc.add_figure_templates(default="mantine_light")


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
        forceColorScheme="light",
        theme={
            "components": {
                "Text": {
                    "defaultProps": {
                        "size": "lg",
                        "ta": "justify",
                    },
                },
                "List": {
                    "defaultProps": {
                        "listStyleType": "disc",
                        "size": "lg",
                        "spacing": "md",
                        "className": "list-outside",
                        "withPadding": True,
                    },
                },
                "ListItem": {
                    "defaultProps": {
                        "ta": "justify",
                        "className": "ml-[1rem]",
                    },
                },
                "Divider": {
                    "defaultProps": {
                        "size": "sm",
                        "my": "lg",
                    },
                },
                "Button": {
                    "defaultProps": {
                        "color": "pink",
                    },
                },
            },
        },
        children=DashboardAppShell(),
    )

    with app.server.app_context():
        dashboard.utils.warmup_cache()

    return app


app = init_app()


def main():
    app.run(debug=True, dev_tools_hot_reload=True)

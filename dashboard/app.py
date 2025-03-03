import dash
from components.sidebar import sidebar
from dash import Dash, dcc, html

app = Dash(
    __name__, use_pages=True, pages_folder="pages", suppress_callback_exceptions=True
)

app.layout = html.Div(
    children=[
        # dcc.location to tracks the current url
        dcc.Location(id="url", refresh=False),
        # Sidebar Toggle Button
        html.Button(
            "☰",
            id="open-sidebar",
            className="text-xl p-2 rounded fixed top-2 left-2 z-40",
        ),
        # sidebar
        sidebar(),
        # main content
        html.Div(
            className="ml-4 mt-10",
            children=[
                html.H1(
                    "An Analysis of the Cost of Living in Singapore",
                    className="text-2xl font-bold text-center",
                ),
                # page container
                html.Div(dash.page_container, className="p-4"),
            ],
        ),
    ]
)


def main():
    app.run(debug=True, dev_tools_hot_reload=True)

from typing import List

import dash
from components.sidebar import sidebar
from dash import ClientsideFunction, Dash, clientside_callback, dcc, html
from dash.dependencies import Input, Output

app = Dash(
    __name__, use_pages=True, pages_folder="pages", suppress_callback_exceptions=True
)

# dynamically fetch pages from dash page
pages = [
    (page["name"], page["relative_path"])
    for page in dash.page_registry.values()
    if page["name"] != "Not found 404"
]

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
        sidebar(pages),
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


# callback to update the sidebar links based on current url
@app.callback(Output("sidebar-links", "children"), [Input("url", "pathname")])
def update_sidebar_links(pathname: str) -> List[html.Li]:
    children = []
    for title, href in pages:
        if pathname == href:
            class_str = "block px-5 py-3 text-[#00ff88] text-xl font-semibold"
        else:
            class_str = "block px-5 py-3 hover:text-[#00ff88] text-xl text-gray-300 font-semibold"
        children.append(html.Li(dcc.Link(title, href=href, className=class_str)))
    return children


# Client-side callback for toggling the sidebar.
clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="toggleSidebar"),
    Output("sidebar", "className"),
    Input("open-sidebar", "n_clicks"),
    Input("close-sidebar", "n_clicks"),
)


def main():
    app.run(debug=True, dev_tools_hot_reload=True)

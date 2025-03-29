from dash import (
    ClientsideFunction,
    Input,
    Output,
    State,
    clientside_callback,
    dcc,
    html,
)

# title: href
LINKS: dict[str, str] = {
    "Home": "/",
    "Taxes": "/taxes",
    "Necessities": "/necessities",
    "Healthcare": "/healthcare",
    "Global": "/global",
}

LINK_CLASSES_DEFAULT: str = (
    "block px-5 py-3 hover:text-[#00ff88] text-xl text-gray-300 font-semibold "
)

LINK_CLASSES_CURRENT_PATH: str = "block px-5 py-3 text-[#00ff88] text-xl font-semibold "


def _id_from_title(title: str) -> str:
    return f"{title.lower()}-sidebar-link"


def sidebar() -> html.Div:
    return html.Div(
        id="sidebar",
        className="fixed left-0 top-0 w-64 bg-gray-800 h-full transform -translate-x-full transition-all duration-300 ease-in-out z-50 shadow-lg",
        children=[
            html.Div(
                className="bg-[#343342] h-16",
                children=[
                    html.Button(
                        html.I(className="fa-solid fa-xmark"),
                        id="close-sidebar",
                        className="absolute top-2 right-2 text-lg p-2 text-gray-200",
                    ),
                    html.H2(
                        "Dashboard", className="text-xl font-bold p-4 text-gray-200"
                    ),
                ],
            ),
            html.Ul(
                id="sidebar-links",
                className="mt-4",
                children=[
                    html.Li(
                        dcc.Link(
                            id=_id_from_title(title),
                            href=href,
                            children=title,
                            className=LINK_CLASSES_DEFAULT,
                        )
                    )
                    for title, href in LINKS.items()
                ],
            ),
        ],
    )


# Client-side callback for toggling the sidebar.
clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="toggleSidebar"),
    Output("sidebar", "className"),
    Input("open-sidebar", "n_clicks"),
    Input("close-sidebar", "n_clicks"),
    Input("url", "pathname"),
)


# Update the sidebar link colours based on the current URL.
clientside_callback(
    ClientsideFunction(
        namespace="clientside", function_name="updateSidebarLinkColours"
    ),
    *(Output(_id_from_title(title), "className") for title in LINKS.keys()),
    Input("url", "pathname"),
    *(State(_id_from_title(title), "href") for title in LINKS.keys()),
)

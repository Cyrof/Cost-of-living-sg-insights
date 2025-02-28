from dash import Input, Output, callback, dcc, html

# title: href
LINKS: dict[str, str] = {
    "Introduction": "/",
    "Taxes": "/taxes",
    "Necessities": "/necessities",
    "Healthcare": "/healthcare",
    "Global": "/global",
    "Conclusion": "/conclusion",
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
                className="bg-[#343342]",
                children=[
                    html.Button(
                        "✖",
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


# Update the sidebar link colours based on the current URL.
@callback(
    *(Output(_id_from_title(title), "className") for title in LINKS.keys()),
    Input("url", "pathname"),
)
def update_sidebar_links(pathname: str) -> tuple[str, ...]:
    return tuple(
        LINK_CLASSES_CURRENT_PATH if href == pathname else LINK_CLASSES_DEFAULT
        for href in LINKS.values()
    )

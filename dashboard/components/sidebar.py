from typing import List, Tuple

from dash import html


def sidebar(links: List[Tuple[str, str]]) -> html.Div:
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
                children=[html.Li(html.A(title, href=href)) for title, href in links],
            ),
        ],
    )

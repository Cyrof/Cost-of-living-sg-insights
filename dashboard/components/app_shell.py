import dash
import dash_mantine_components as dmc
from dash import (ClientsideFunction, Input, Output, State,
                  clientside_callback, dcc, html)

# title: href
LINKS: dict[str, str] = {
    "Home": "/",
    "Taxes": "/taxes",
    "Necessities": "/necessities",
    "Healthcare": "/healthcare",
    "Global": "/global",
}


HEADER_FOOTER_BG: str = "pink"
HEADER_FOOTER_C: str = "white"

SIDEBAR_BG: str = "gray.0"
NAVLINK_COLOR: str = "pink"

# This is applied using Tailwind, so it must be a valid colour string,
# not Mantine's colour names / shades.
NAVLINK_HOVER_BG: str = dmc.DEFAULT_THEME["colors"]["gray"][1]


def _id_from_title(title: str) -> str:
    return f"{title.lower()}-sidebar-link"


def DashboardAppShell() -> dmc.AppShell:
    return dmc.AppShell(
        id="appshell",
        header={"height": 80},
        navbar={
            "width": 300,
            "breakpoint": "sm",
            "collapsed": {"mobile": False, "desktop": False},
        },
        padding=0,
        children=[
            # Stores the current URL for access in callbacks.
            DashboardHeader(),
            DashboardNavbar(),
            dmc.AppShellMain(
                children=[
                    dmc.Space(h="xl"),
                    # Page content
                    dmc.Group(
                        dmc.Box(
                            dash.page_container,
                            w=1000,
                            p="xl",
                        ),
                        align="center",
                        justify="center",
                    ),
                    dmc.Space(h="xl"),
                    DashboardFooter(),
                ],
            ),
            html.Div(
                id="sidebar-overlay",
                className="hidden fixed top-0 left-0 w-screen h-screen bg-gray-500 opacity-50 z-40",
                n_clicks=0,
            ),
        ],
    )


def DashboardHeader() -> dmc.AppShellHeader:
    return dmc.AppShellHeader(
        id="header",
        bg=HEADER_FOOTER_BG,
        c=HEADER_FOOTER_C,
        children=dmc.Group(
            h="100%",
            px="md",
            wrap="nowrap",
            children=[
                dmc.Burger(
                    id="mobile-burger",
                    color="white",
                    hiddenFrom="sm",
                    opened=False,
                ),
                dmc.Burger(
                    id="desktop-burger",
                    color="white",
                    visibleFrom="sm",
                    opened=False,
                ),
                dmc.Title(
                    "An Analysis of the Cost of Living in Singapore",
                    order=3,
                    lineClamp=1,
                ),
            ],
        ),
    )


def DashboardNavbar() -> dmc.AppShellNavbar:
    return dmc.AppShellNavbar(
        id="navbar",
        p="xl",
        bg=SIDEBAR_BG,
        children=[
            dcc.Location(id="url", refresh=False),
            dmc.Stack(
                children=[
                    dmc.Title("Dashboard Navigation", order=3),
                    dmc.Divider(my=0),
                    *(
                        dmc.NavLink(
                            id=_id_from_title(title),
                            label=title,
                            href=href,
                            color=NAVLINK_COLOR,
                            classNames={
                                "root": f"hover:bg-[{NAVLINK_HOVER_BG}]",
                                "label": "text-xl",
                            },
                        )
                        for title, href in LINKS.items()
                    ),
                ]
            ),
        ],
    )


def DashboardFooter() -> dmc.Stack:
    names = [
        "Keith Neo Kai Si",
        "Dixon Sean Low Yan Feng",
        "Styverson Ng Yu Hao",
        "Atilla Tanay",
    ]
    return dmc.Stack(
        id="footer",
        p="xl",
        bg=HEADER_FOOTER_BG,
        c=HEADER_FOOTER_C,
        children=[
            dmc.Title("Project Team", ta="center", order=4),
            dmc.Group(
                [dmc.Text(name, fw=500) for name in names],
                justify="center",
            ),
            dmc.Text(
                "© 2025 Cost of Living in Singapore Dashboard. All rights reserved.",
                size="xs",
                ta="center",
            ),
        ],
        gap="lg",
    )


clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="updateSidebarState"),
    [
        Output("appshell", "navbar"),
        Output("sidebar-overlay", "style"),
        Output("mobile-burger", "opened"),
        Output("desktop-burger", "opened"),
    ],
    [
        Input("mobile-burger", "opened"),
        Input("desktop-burger", "opened"),
        Input("url", "pathname"),
        Input("sidebar-overlay", "n_clicks"),
    ],
    State("appshell", "navbar"),
)

# Update the sidebar link colours based on the current URL.
clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="setActiveNavLink"),
    *(Output(_id_from_title(title), "active") for title in LINKS.keys()),
    Input("url", "pathname"),
    *(State(_id_from_title(title), "href") for title in LINKS.keys()),
)

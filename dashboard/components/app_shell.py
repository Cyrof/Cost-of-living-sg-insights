import dash
import dash_mantine_components as dmc
from dash import (ClientsideFunction, Input, Output, State,
                  clientside_callback, dcc)

# title: href
LINKS: dict[str, str] = {
    "Home": "/",
    "Taxes": "/taxes",
    "Necessities": "/necessities",
    "Healthcare": "/healthcare",
    "Global": "/global",
}

LINK_CLASSES_DEFAULT: str = "hover:text-[#00ff88]"

LINK_CLASSES_CURRENT_PATH: str = "block px-5 py-3 text-[#00ff88] text-xl font-semibold "


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
                    dmc.Space(h="lg"),
                    # Page content
                    dmc.Group(
                        dmc.Box(
                            dash.page_container,
                            w=1000,
                            p="lg",
                        ),
                        align="center",
                        justify="center",
                    ),
                    dmc.Space(h="lg"),
                    DashboardFooter(),
                ],
            ),
        ],
    )


def DashboardHeader() -> dmc.AppShellHeader:
    return dmc.AppShellHeader(
        id="header",
        bg="indigo.6",
        c="white",
        children=dmc.Group(
            h="100%",
            px="md",
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
                ),
            ],
        ),
    )


def DashboardNavbar() -> dmc.AppShellNavbar:
    return dmc.AppShellNavbar(
        id="navbar",
        p="xl",
        bg="gray.0",
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
                            classNames={"label": "text-xl"},
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
        bg="indigo.6",
        c="white",
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


# Client-side callback for toggling the sidebar.
clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="toggleSidebar"),
    Output("appshell", "navbar"),
    Input("mobile-burger", "opened"),
    Input("desktop-burger", "opened"),
    State("appshell", "navbar"),
)

# Update the sidebar link colours based on the current URL.
clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="setActiveNavLink"),
    *(Output(_id_from_title(title), "active") for title in LINKS.keys()),
    Input("url", "pathname"),
    *(State(_id_from_title(title), "href") for title in LINKS.keys()),
)

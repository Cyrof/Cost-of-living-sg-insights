import dash_mantine_components as dmc
from dash import html

def topbar() -> dmc.Box:
    return dmc.Box(
        className="fixed top-0 left-0 right-0 h-16 bg-palette2 z-50 flex items-center px-4",
        children = [
            # hamburger icon on left side
            dmc.ActionIcon(
                html.I(className="fa-solid fa-bars text-3xl text-palette1 hover:text-gray-400"),
                id="open-sidebar",
                variant="transparent",
            ),
            # Main title in center
            dmc.Title(
                "An Analysis of the Cost of Living in Singapore",
                size="xl",
                className="flex-1 text-center text-palette1",
            ),
            # right dummy data
            dmc.ActionIcon(
                html.I(className="fa-solid fa-bars"),
                className="opacity-0",
                variant="light",
                radius="xl"
            )
        ],
    )

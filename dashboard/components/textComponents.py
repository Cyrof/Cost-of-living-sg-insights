from typing import Any

import dash_mantine_components as dmc
from dash import MATCH, Input, Output, State, callback
from plotly.graph_objects import Figure

from dashboard.components.graphWrapper import graphWrapper


def create_card(title: str, description: str, className: str = "") -> dmc.Paper:
    return dmc.Paper(
        [
            dmc.Stack(
                [
                    dmc.Text(title, className="text-2xl font-bold"),
                    dmc.Divider(className="my-2", size="sm"),
                    dmc.Text(
                        description,
                        className="text-base font-normal leading-relaxed",
                    ),
                ],
                className="p-6",
            )
        ],
        shadow="sm",
        radius="lg",
        className=f"transition-all duration-300 hover:shadow-xl {className}",
        withBorder=True,
        style={
            "borderWidth": "2px",
            "height": "100%",
        },
    )


def create_card_graph(
    title: str,
    short_desc: str,
    full_desc: str,
    graphs: list[tuple[str, Figure] | tuple[str, Figure, dict[str, Any]]],
    className: str = "",
) -> dmc.Paper:
    if len(graphs) == 1:
        kwargs = graphs[0][2] if len(graphs[0]) > 2 else dict()
        graph_component = graphWrapper(graphs[0][0], graphs[0][1], **kwargs)
    else:
        graph_component = dmc.Stack(
            [
                graphWrapper(graph_id, fig, **kwargs)
                for graph_id, fig, kwargs in (
                    (
                        graph_tuple
                        if len(graph_tuple) > 2
                        else (graph_tuple[0], graph_tuple[1], dict())
                    )
                    for graph_tuple in graphs
                )
            ],
        )

    return dmc.Paper(
        [
            dmc.Stack(
                [
                    # title
                    dmc.Text(title, className="text-2xl font-bold"),
                    dmc.Divider(className="my-2", size="sm"),
                    # graph
                    graph_component,
                    # short description
                    dmc.Text(
                        short_desc,
                        id=f"{graphs[0][0]}-short-desc",
                        className="text-base font-normal loading-relaxed mt-4",
                    ),
                    # collapsible desc
                    dmc.Collapse(
                        [
                            dmc.Text(
                                full_desc,
                                className="text-base font-normal loading-relaxed",
                            ),
                        ],
                        id={"type": "collapse-desc", "index": graphs[0][0]},
                    ),
                    # toggle button
                    dmc.Button(
                        "Read More",
                        id={"type": "toggle-desc", "index": graphs[0][0]},
                        variant="outline",
                        size="sm",
                        className="mt-4",
                    ),
                ],
                className="p-6",
            )
        ],
        shadow="sm",
        radius="lg",
        className=f"transition-all duration-300 hover:shadow-xl {className}",
        withBorder=True,
        style={
            "borderWidth": "2px",
            "height": "100%",
        },
    )


def create_section_title(title: str) -> dmc.Group:
    return dmc.Stack(
        children=[
            dmc.Divider(),
            dmc.Title(title, order=1),
            dmc.Divider(),
        ],
    )


@callback(
    [
        Output({"type": "collapse-desc", "index": MATCH}, "in"),
        Output({"type": "toggle-desc", "index": MATCH}, "children"),
    ],
    Input({"type": "toggle-desc", "index": MATCH}, "n_clicks"),
    State({"type": "collapse-desc", "index": MATCH}, "in"),
)
def toggle_card_ssr(n_clicks, is_open):
    if not n_clicks:
        return False, "Read More"
    # Toggle based on the click count: odd -> open, even -> closed.
    if n_clicks % 2 == 1:
        return True, "Show Less"
    else:
        return False, "Read More"

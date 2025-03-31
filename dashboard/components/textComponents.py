from typing import Any

import dash_mantine_components as dmc
from dash import (MATCH, ClientsideFunction, Input, Output, State,
                  clientside_callback)
from plotly.graph_objects import Figure

from dashboard.components.graphWrapper import graphWrapper


def create_card(
    title: str,
    description: str,
    className: str = "",
    stackGap: str | int = "md",
    dividerKwargs: dict[str, Any] | None = None,
) -> dmc.Paper:
    dividerKwargs = dividerKwargs or {"className": "my-2", "size": "sm"}
    return dmc.Paper(
        [
            dmc.Stack(
                gap=stackGap,
                className="p-6",
                children=[
                    dmc.Text(title, className="text-2xl font-bold"),
                    dmc.Divider(**dividerKwargs),
                    dmc.Text(
                        description,
                        className="text-base font-normal leading-relaxed",
                    ),
                ],
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
    short_desc: str | Any,
    full_desc: str | Any,
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
        shadow="sm",
        radius="lg",
        mb="md",
        p="xl",
        className=f"transition-all duration-300 hover:shadow-xl {className}",
        withBorder=True,
        style={
            "borderWidth": "2px",
            "height": "100%",
        },
        children=dmc.Stack(
            children=[
                # title
                dmc.Title(title, order=3),
                dmc.Divider(my="sm"),
                # graph
                graph_component,
                # short description
                (
                    dmc.Text(
                        id=f"{graphs[0][0]}-short-desc",
                        children=short_desc,
                    )
                    if isinstance(short_desc, str)
                    else short_desc
                ),
                # collapsible desc
                dmc.Collapse(
                    id={"type": "collapse-desc", "index": graphs[0][0]},
                    children=(
                        [dmc.Text(full_desc)]
                        if isinstance(full_desc, str)
                        else full_desc
                    ),
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
        ),
    )


def create_page_title(
    title: str, subtitle: str | None = None, centered: bool = True
) -> dmc.Group:
    content_children = [
        dmc.Title(title, order=1, ta="center" if centered else "left"),
    ]

    if subtitle:
        content_children.append(
            dmc.Title(
                subtitle, order=3, opacity="70%", ta="center" if centered else "left"
            )
        )

    content = dmc.Stack(
        gap=2,
        align="center" if centered else "flex-start",
        children=content_children,
    )

    return dmc.Stack(
        mb="lg",
        children=[
            dmc.Divider(my=0),
            content,
            dmc.Divider(my=0),
        ],
    )


def create_section_title(title: str) -> dmc.Group:
    return dmc.Title(title, order=2)


# For toggling "Read more".
clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="toggleCard"),
    Output({"type": "collapse-desc", "index": MATCH}, "in"),
    Output({"type": "toggle-desc", "index": MATCH}, "children"),
    Input({"type": "toggle-desc", "index": MATCH}, "n_clicks"),
    State({"type": "collapse-desc", "index": MATCH}, "in"),
)

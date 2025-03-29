import dash_mantine_components as dmc
from components.graphWrapper import graphWrapper
from plotly.graph_objects import Figure
from dash import Input, Output, State, MATCH, callback


def create_card(title: str, description: str, className: str = "") -> dmc.Paper:
    return dmc.Paper(
        [
            dmc.Stack(
                [
                    dmc.Text(title, className="text-2xl font-bold text-palette3"),
                    dmc.Divider(className="my-2", color="var(--palette3)", size="sm"),
                    dmc.Text(
                        description,
                        className="text-base font-normal text-palette3 leading-relaxed",
                    ),
                ],
                className="p-6",
            )
        ],
        shadow="sm",
        radius="lg",
        className=f"bg-white transition-all duration-300 hover:shadow-xl {className}",
        withBorder=True,
        style={
            "borderColor": "var(--palette3)",
            "borderWidth": "2px",
            "height": "100%",
        },
    )


def create_card_graph(
    title: str,
    short_desc: str,
    full_desc: str,
    graphs: list[tuple[str, Figure]],
    # figure: Figure,
    # card_id: str,
    className: str = "",
) -> dmc.Paper:
    if len(graphs) == 1:
        graph_component = graphWrapper(graphs[0][0], graphs[0][1])
    else:
        graph_component = dmc.Group(
            [graphWrapper(graph_id, fig) for graph_id, fig in graphs],
            align="start",
            grow=True,
        )

    return dmc.Paper(
        [
            dmc.Stack(
                [
                    # title
                    dmc.Text(title, className="text-2xl font-bold text-palette3"),
                    dmc.Divider(className="my-2", color="var(--palette3)", size="sm"),
                    # graph
                    # graphWrapper(card_id, figure),
                    graph_component,
                    # short description
                    dmc.Text(
                        short_desc,
                        id=f"{graphs[0][0]}-short-desc",
                        className="text-base font-normal text-palette3 loading-relaxed mt-4",
                    ),
                    # collapsible desc
                    dmc.Collapse(
                        [
                            dmc.Text(
                                full_desc,
                                className="text-base font-normal text-palette3 loading-relaxed",
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
        className=f"bg-white transition-all duration-300 hover:shadow-xl {className}",
        withBorder=True,
        style={
            "borderColor": "var(--palette3)",
            "borderWidth": "2px",
            "height": "100%",
        },
    )


def create_section_title(title: str) -> dmc.Group:
    return dmc.Group(
        [
            dmc.Divider(className="flex-grow", color="var(--palette2)", size="xs"),
            dmc.Text(title, className="text-3xl font-bold mx-4 text-palette4"),
            dmc.Divider(className="flex-grow", color="var(--palette2)", size="xs"),
        ],
        justify="center",
        className="my-6",
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

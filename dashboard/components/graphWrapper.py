import textwrap

import dash_mantine_components as dmc
from dash import dcc
from plotly.graph_objects import Figure


def graphWrapper(id: str, figure: Figure, scale: float = 1.0) -> dmc.Box:
    # Strip surrounding whitespace and wrap the legend's text.
    for trace in figure.data:
        if trace.name:
            original_name = trace.name
            wrapped_name_list = textwrap.wrap(original_name.strip(), width=20)
            trace.name = "<br>".join(wrapped_name_list)

        # Wrap heatmap colorbar title.
        if "colorbar" in trace:
            original_colorbar_title = trace.colorbar.title.text
            trace.colorbar.title.text = "<br>".join(
                textwrap.wrap(original_colorbar_title.strip(), width=20)
            )

    figure.update_layout(template="mantine_light")

    return dmc.Box(
        children=[
            dcc.Graph(
                id=id,
                figure=figure,
                className="w-auto h-auto flex-1",
                responsive=True,
                config={"displaylogo": False},
                style={"transform": f"scale({scale})"},
            ),
        ],
        className="w-100",
    )

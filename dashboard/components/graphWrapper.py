import dash_mantine_components as dmc
from plotly.graph_objects import Figure
from dash import dcc

def graphWrapper(id: str, figure: Figure) -> dmc.Box:
    return dmc.Box(
        children=[
            dcc.Graph(
                id=id,
                figure=figure,
                className="w-[90%] h-auto",
                responsive=True
            ),
        ],
        className="rounded-xl flex justify-center bg-white"
    )
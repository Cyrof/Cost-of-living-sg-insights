import plotly.express as px
from dash import Dash, dcc, html

app = Dash()

test_data: dict[str, list[int]] = {
    "x": list(range(0, 10)),
    "y": list(range(0, 10)),
}

app.layout = [
    html.H1(children="Title of Dash App", style={"textAlign": "center"}),
    dcc.Graph(id="graph-content", figure=px.line(test_data, x="x", y="y")),
]


def main():
    app.run(debug=True)

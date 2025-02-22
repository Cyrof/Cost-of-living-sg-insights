import dash
from dash import Dash, dcc, html

app = Dash(use_pages=True, pages_folder="pages")

app.layout = html.Div(
    [
        html.H1(
            "An Analysis of the Cost of Living in Singapore",
            style={"textAlign": "center"},
        ),
        html.Div(
            [
                html.Div(dcc.Link(f"{page["name"]}", href=page["relative_path"]))
                for page in dash.page_registry.values()
                if page["name"] != "Not found 404"  # Filter out the 404 page.
            ]
        ),
        dash.page_container,
    ]
)


def main():
    app.run(debug=True)

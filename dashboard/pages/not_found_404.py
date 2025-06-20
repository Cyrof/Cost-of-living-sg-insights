import dash
import dash_mantine_components as dmc

dash.register_page(__name__)


def layout():
    return dmc.Center(
        bg="pink.4",
        children=[
            dmc.Stack(
                align="center",
                gap="md",
                children=[
                    dmc.Text("404", className="font-semibold text-8xl text-gray-800"),
                    dmc.Image(
                        src="/assets/images/oia-uia.gif",
                        alt="uiia",
                        # className="w-1/2 h-auto"
                    ),
                    dmc.Text(
                        "Page Not Found",
                        className="font-semibold text-3xl text-gray-800",
                    ),
                    dmc.Anchor(
                        href="/",
                        children=[
                            dmc.Button(
                                "Go Home",
                                className="rounded-lg",
                            )
                        ],
                    ),
                ],
            )
        ],
        className="fixed left-0 top-0 min-h-screen w-screen z-[9999]",
    )

import dash_mantine_components as dmc
from datetime import datetime


def footer() -> dmc.Stack:
    current_year = datetime.now().year

    return dmc.Stack(
        [
            # project description
            dmc.Text(
                "Project Team", className="text-3xl text-white font-bold", ta="center"
            ),
            dmc.Group(
                [
                    dmc.Text(
                        "Keith Neo Kai Si", className="text-md text-white font-semibold"
                    ),
                    dmc.Text(
                        "Dixon Sean Low Yan Feng",
                        className="text-md text-white font-semibold",
                    ),
                    dmc.Text(
                        "Styverson Ng Yu Hao",
                        className="text-md text-white font-semibold",
                    ),
                    dmc.Text(
                        "Atilla Tanay", className="text-md text-white font-semibold"
                    ),
                ],
                justify="center",
                className="mt-2 space-x-4",
            ),
            dmc.Text(
                # probably should change this
                "© 2025 Cost of Living in Singapore Dashboard. All rights reserved.",
                className="text-sm text-stone-200",
                ta="center",
            ),
        ],
        className="py-8",
        gap="lg",
    )

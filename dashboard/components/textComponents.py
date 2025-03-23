import dash_mantine_components as dmc

def create_card(title: str, description: str, className: str = "") -> dmc.Paper:
    return dmc.Paper(
        [
            dmc.Stack(
                [
                    dmc.Text(
                        title,
                        className="text-2xl font-bold text-palette3"
                    ),
                    dmc.Divider(
                        className="my-2",
                        color="var(--palette3)",
                        size="sm"
                    ),
                    dmc.Text(
                        description, 
                        className="text-base font-normal text-palette3 leading-relaxed"
                    ),
                ],
                className="p-6"
            )
        ],
        shadow="sm",
        radius="lg",
        className=f"bg-palette1 transition-all duration-300 hover:shadow-xl {className}",
        withBorder=True,
        style={
            "borderColor": "var(--palette3)",
            "borderWidth": "2px",
            "height": "100%"
        }
    )


def create_section_title(title: str) -> dmc.Group:
    return dmc.Group(
        [
            dmc.Divider(
                className="flex-grow",
                color="var(--palette2)",
                size="xs"
            ),
            dmc.Text(
                title,
                className="text-3xl font-bold mx-4 text-palette4"
            ),
            dmc.Divider(
                className="flex-grow",
                color="var(--palette2)",
                size="xs"
            ),
        ],
        justify="center",
        className="my-6"
    )

import functools
import os.path

import plotly.io
from flask import current_app as flask_app
from plotly.graph_objects import Figure

CHARTS_DIR: str = "data/charts"


@functools.cache
def load_chart_json(filename: str) -> Figure:
    with flask_app.open_resource(os.path.join(CHARTS_DIR, filename)) as file:
        return plotly.io.from_json(file.read())


def load_global_charts() -> dict[str, Figure]:
    return {
        "cpi_bubble_map": load_chart_json("cpi_bubble_map.json"),
        "gdp_bubble_map": load_chart_json("gdp_bubble_map.json"),
        "cpi_vs_gdp_bubble_chart": load_chart_json("cpi_vs_gdp_bubble_chart.json"),
    }


def load_necessities_charts() -> dict[str, Figure]:
    return {
        "necessities_cpi_breakdown": load_chart_json("necessities_cpi_breakdown.json"),
        "necessities_cpi_vs_income": load_chart_json("necessities_cpi_vs_income.json"),
        "monthly_expenditure_donut": load_chart_json("monthly_expenditure_donut.json"),
    }


def load_healthcare_charts() -> dict[str, Figure]:
    return {
        "life_expectancy_vs_healthcare_cpi": load_chart_json(
            "life_expectancy_vs_healthcare_cpi.json"
        ),
        "healthcare_cpi_vs_gross_monthly_income": load_chart_json(
            "healthcare_cpi_vs_gross_monthly_income.json"
        ),
        "percentage_change_in_healthcare_cpi_and_income": load_chart_json(
            "percentage_change_in_healthcare_cpi_and_income.json"
        ),
        "healthcare_cpi_breakdown": load_chart_json("healthcare_cpi_breakdown.json"),
    }


def load_taxes_charts() -> dict[str, Figure]:
    return {
        "iras_tax_collection_bar": load_chart_json("iras_tax_collection_bar.json"),
        "cpi_vs_gst_line_bar": load_chart_json("cpi_vs_gst_line_bar.json"),
        "income_tax_rates_step_line": load_chart_json(
            "income_tax_rates_step_line.json"
        ),
        "income_tax_heatmap": load_chart_json("income_tax_heatmap.json"),
        "property_tax_rates_step_line": load_chart_json(
            "property_tax_rates_step_line.json"
        ),
        "property_tax_collection_annual_value_bubble": (
            load_chart_json("property_tax_collection_annual_value_bubble.json")
        ),
    }


def load_home_charts() -> dict[str, Figure]:
    return {
        "percentage_change_in_healthcare_cpi_and_income": load_chart_json(
            "percentage_change_in_healthcare_cpi_and_income.json"
        ),
        "cpi_vs_gst_line_bar": load_chart_json("cpi_vs_gst_line_bar.json"),
        "necessities_cpi_vs_income": load_chart_json("necessities_cpi_vs_income.json"),
        "cpi_bubble_map": load_chart_json("cpi_bubble_map.json"),
    }


def warmup_cache() -> None:
    load_global_charts()
    load_necessities_charts()
    load_healthcare_charts()
    load_taxes_charts()
    # No need to call `load_home_charts()` because all charts should already
    # have been cached by the above.

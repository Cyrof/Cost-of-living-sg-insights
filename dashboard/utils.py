import functools
from typing import Any

import plotly.io
from plotly.graph_objects import Figure

from dashboard.data.cpi_bubble_map import CPI_BUBBLE_MAP
from dashboard.data.cpi_vs_gdp_bubble_chart import CPI_VS_GDP_BUBBLE_CHART
from dashboard.data.cpi_vs_gst_line_bar import CPI_VS_GST_LINE_BAR
from dashboard.data.gdp_bubble_map import GDP_BUBBLE_MAP
from dashboard.data.healthcare_cpi_breakdown import HEALTHCARE_CPI_BREAKDOWN
from dashboard.data.healthcare_cpi_vs_gross_monthly_income import \
    HEALTHCARE_CPI_VS_GROSS_MONTHLY_INCOME
from dashboard.data.income_tax_heatmap import INCOME_TAX_HEATMAP
from dashboard.data.income_tax_rates_step_line import \
    INCOME_TAX_RATES_STEP_LINE
from dashboard.data.iras_tax_collection_bar import IRAS_TAX_COLLECTION_BAR
from dashboard.data.life_expectancy_vs_healthcare_cpi import \
    LIFE_EXPECTANCY_VS_HEALTHCARE_CPI
from dashboard.data.monthly_expenditure_donut import MONTHLY_EXPENDITURE_DONUT
from dashboard.data.necessities_cpi_breakdown import NECESSITIES_CPI_BREAKDOWN
from dashboard.data.necessities_cpi_vs_income import NECESSITIES_CPI_VS_INCOME
from dashboard.data.percentage_change_in_healthcare_cpi_and_income import \
    PERCENTAGE_CHANGE_IN_HEALTHCARE_CPI_AND_INCOME
from dashboard.data.property_tax_collection_annual_value_bubble import \
    PROPERTY_TAX_COLLECTION_ANNUAL_VALUE_BUBBLE
from dashboard.data.property_tax_rates_step_line import \
    PROPERTY_TAX_RATES_STEP_LINE


@functools.cache
def load_chart_json(json: str) -> Figure:
    return plotly.io.from_json(json)


def load_global_charts() -> dict[str, Figure]:
    return {
        "cpi_bubble_map": load_chart_json(CPI_BUBBLE_MAP),
        "gdp_bubble_map": load_chart_json(GDP_BUBBLE_MAP),
        "cpi_vs_gdp_bubble_chart": load_chart_json(CPI_VS_GDP_BUBBLE_CHART),
    }


def load_necessities_charts() -> dict[str, Figure]:
    monthly_expenditure_donut = load_chart_json(MONTHLY_EXPENDITURE_DONUT)
    monthly_expenditure_donut.update_layout(
        margin=dict(t=40, l=0, r=0, b=10),
    )

    return {
        "necessities_cpi_breakdown": load_chart_json(NECESSITIES_CPI_BREAKDOWN),
        "necessities_cpi_vs_income": load_chart_json(NECESSITIES_CPI_VS_INCOME),
        "monthly_expenditure_donut": monthly_expenditure_donut,
    }


def load_healthcare_charts() -> dict[str, Figure]:
    healthcare_cpi_vs_gross_monthly_income = load_chart_json(
        HEALTHCARE_CPI_VS_GROSS_MONTHLY_INCOME
    )
    healthcare_cpi_vs_gross_monthly_income.update_layout(
        legend=dict(
            x=1.05,
            xanchor="left",
        ),
    )

    return {
        "life_expectancy_vs_healthcare_cpi": load_chart_json(
            LIFE_EXPECTANCY_VS_HEALTHCARE_CPI
        ),
        "healthcare_cpi_vs_gross_monthly_income": healthcare_cpi_vs_gross_monthly_income,
        "percentage_change_in_healthcare_cpi_and_income": load_chart_json(
            PERCENTAGE_CHANGE_IN_HEALTHCARE_CPI_AND_INCOME
        ),
        "healthcare_cpi_breakdown": load_chart_json(HEALTHCARE_CPI_BREAKDOWN),
    }


def load_taxes_charts() -> dict[str, Figure]:
    cpi_vs_gst_line_bar = load_chart_json(CPI_VS_GST_LINE_BAR)
    cpi_vs_gst_line_bar.update_layout(
        legend=dict(
            x=1.05,
            xanchor="left",
        ),
    )

    return {
        "iras_tax_collection_bar": load_chart_json(IRAS_TAX_COLLECTION_BAR),
        "cpi_vs_gst_line_bar": cpi_vs_gst_line_bar,
        "income_tax_rates_step_line": load_chart_json(INCOME_TAX_RATES_STEP_LINE),
        "income_tax_heatmap": load_chart_json(INCOME_TAX_HEATMAP),
        "property_tax_rates_step_line": load_chart_json(PROPERTY_TAX_RATES_STEP_LINE),
        "property_tax_collection_annual_value_bubble": (
            load_chart_json(PROPERTY_TAX_COLLECTION_ANNUAL_VALUE_BUBBLE)
        ),
    }


def load_home_charts() -> dict[str, Figure]:
    return {
        "percentage_change_in_healthcare_cpi_and_income": load_chart_json(
            PERCENTAGE_CHANGE_IN_HEALTHCARE_CPI_AND_INCOME
        ),
        "iras_tax_collection_bar": load_chart_json(IRAS_TAX_COLLECTION_BAR),
        "necessities_cpi_vs_income": load_chart_json(NECESSITIES_CPI_VS_INCOME),
        "cpi_bubble_map": load_chart_json(CPI_BUBBLE_MAP),
    }


def warmup_cache() -> None:
    load_global_charts()
    load_necessities_charts()
    load_healthcare_charts()
    load_taxes_charts()
    # No need to call `load_home_charts()` because all charts should already
    # have been cached by the above.


def intersperse(lst: list, item: Any):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

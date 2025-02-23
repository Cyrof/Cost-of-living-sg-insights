from dataclasses import dataclass
from enum import Enum, auto


class Source(Enum):
    DataGov = auto()
    SingStat = auto()
    WorldBank = auto()


@dataclass
class Dataset:
    source: Source
    id: str


DEFAULT_DATASETS: dict[str, Dataset] = {
    "global_cpi": Dataset(Source.WorldBank, "CPTOTSAXN"),
    "global_gdp": Dataset(Source.WorldBank, "NY.GDP.PCAP.PP.KD"),
    "global_reer2010": Dataset(Source.WorldBank, "PX.REX.REER"),
    "sg_cpi_annual": Dataset(Source.DataGov, "d_dcb352661fb449c4a4c0ab23aa8d6399"),
    "sg_iras_tax_id": Dataset(Source.DataGov, "d_21e22578cabce897e8b27801e5596140"),
    "sg_property_tax_rates_id": Dataset(
        Source.DataGov, "d_2109ad1eafff52dab388f9bcd8148a35"
    ),
    "sg_hdb_annual_value_tax_id": Dataset(
        Source.DataGov, "d_48143be392f1ed22f0700835212e5a60"
    ),
    "sg_gst_id": Dataset(Source.DataGov, "d_2e65ed309aa8d449d1bd0c7ef7c7e4da"),
    "sg_income_tax_rates_id": Dataset(
        Source.DataGov, "d_f73055c69144d2e7734c28811d3982aa"
    ),
    "sg_individual_income_tax_id": Dataset(
        Source.DataGov, "d_f394f202534237671d39b17bd3b506ec"
    ),
    "sg_gross_income_id": Dataset(Source.DataGov, "d_52760e82e8786bac11cca40eb29d1a93"),
    "sg_expenditure_id": Dataset(Source.SingStat, "D10072"),
    "sg_life_expectancy_id": Dataset(Source.SingStat, "M810501"),
}

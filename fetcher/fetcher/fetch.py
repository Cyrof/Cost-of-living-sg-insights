import json
from collections.abc import Sequence
from datetime import datetime
from typing import TypeAlias

import requests
import wbdata

BASE_DATA_GOV_URL: str = "https://data.gov.sg/api/action/datastore_search"
BASE_SINGSTAT_URL: str = "https://tablebuilder.singstat.gov.sg/api/table/tabledata"

DEFAULT_LIMIT: int = 10_000_000


JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None


def fetch_datagov_dataset(dataset_id: str, limit: int = DEFAULT_LIMIT) -> JSON:
    response = requests.get(
        BASE_DATA_GOV_URL,
        params={
            "resource_id": dataset_id,
            "limit": str(limit),
        },
    )

    if not response.ok:
        raise Exception(f"Failed to fetch DataGov dataset ({dataset_id}): {response}.")

    return response.json()


def fetch_singstat_dataset(dataset_id: str, limit: int = DEFAULT_LIMIT) -> JSON:
    response = requests.get(
        f"{BASE_SINGSTAT_URL}/{dataset_id}",
        params={
            "limit": str(limit),
        },
        headers={
            "Accept": "application/json",
            # Need to fake the user agent because SingStat blocks `python-requests`.
            "User-Agent": "curl/8.11.1",
        },
    )

    if not response.ok:
        raise Exception(f"Failed to fetch SingStat dataset ({dataset_id}): {response}.")

    return response.json()


def fetch_worldbank_dataset(
    indicators: dict[str, str],
    country: str | Sequence[str] = "all",
    date: str | datetime | tuple[str | datetime, str | datetime] | None = None,
    freq: str = "Y",
    source: int | str | Sequence[int | str] | None = None,
    parse_dates: bool = False,
    keep_levels: bool = False,
    skip_cache: bool = False,
) -> JSON:
    df = wbdata.get_dataframe(
        indicators=indicators,
        country=country,
        date=date,
        freq=freq,
        source=source,
        parse_dates=parse_dates,
        keep_levels=keep_levels,
        skip_cache=skip_cache,
    )

    df_json_string: str = df.to_json(orient="split")
    df_json: JSON = json.loads(df_json_string)
    return df_json

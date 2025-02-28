import io
import json
import typing
from parser.types import (DataGovJSON, DataGovJSONValidator, SingStatJSON,
                          SingStatJSONColumn, SingStatJSONColumnLeaf,
                          SingStatJSONColumnParent, SingStatJSONRow,
                          SingStatJSONValidator, WorldBankJSON,
                          WorldBankJSONValidator)
from typing import Any

import aiofiles
import pandas as pd


async def parse_datagov_dataset(path: str) -> pd.DataFrame:
    async with aiofiles.open(path, "r") as file:
        content = await file.read()

    data_raw: Any = json.loads(content)
    data: DataGovJSON = DataGovJSONValidator.validate_python(data_raw)

    return pd.DataFrame(data["result"]["records"])


def flatten_singstat_dataset(
    data: (
        list[SingStatJSONRow]
        | list[SingStatJSONColumn]
        | SingStatJSONRow
        | SingStatJSONColumn
    ),
    parent_keys: tuple[str, ...] = (),
) -> list[tuple[str, ...]]:
    records: list[tuple[str, ...]] = []

    if isinstance(data, list):
        data = typing.cast(list[SingStatJSONRow] | list[SingStatJSONColumn], data)
        item: SingStatJSONRow | SingStatJSONColumn
        for item in data:
            records.extend(flatten_singstat_dataset(item, parent_keys))
        return records

    assert isinstance(data, dict)
    data = typing.cast(SingStatJSONRow | SingStatJSONColumn, data)

    new_keys: tuple[str, ...] = parent_keys

    # SingStatJSONRow
    if "rowText" in data:
        data = typing.cast(SingStatJSONRow, data)
        new_keys += (data["rowText"],)
        records.extend(flatten_singstat_dataset(data["columns"], new_keys))
        return records

    # Must be a SingStatJSONColumn if it is not a SingStatJSONRow.
    assert "key" in data

    data = typing.cast(SingStatJSONColumn, data)
    new_keys += (data["key"],)

    # If "value" exists, it is a leaf.
    if "value" in data:
        data = typing.cast(SingStatJSONColumnLeaf, data)
        records.append(new_keys + (data["value"],))
        return records

    # Must be a non-leaf, so recurse deeper.
    assert "columns" in data
    data = typing.cast(SingStatJSONColumnParent, data)
    records.extend(flatten_singstat_dataset(data["columns"], new_keys))
    return records


async def parse_singstat_dataset(path: str) -> pd.DataFrame:
    async with aiofiles.open(path, "r") as file:
        content = await file.read()

    data_raw: Any = json.loads(content)
    data: SingStatJSON = SingStatJSONValidator.validate_python(data_raw)
    records = flatten_singstat_dataset(data["Data"]["row"])
    return pd.DataFrame(records)


async def parse_worldbank_dataset(path: str) -> pd.DataFrame:
    async with aiofiles.open(path, "r") as file:
        content = await file.read()

    # Validate.
    data_raw: Any = json.loads(content)
    _: WorldBankJSON = WorldBankJSONValidator.validate_python(data_raw)

    return pd.read_json(io.StringIO(content), orient="records")

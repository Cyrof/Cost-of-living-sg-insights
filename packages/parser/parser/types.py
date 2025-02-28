from typing import Any, TypeAlias, TypedDict

from pydantic import TypeAdapter

JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None

DataGovJSONLinks = TypedDict(
    "DataGovJSONLinks",
    {
        "start": str,
        "next": str,
    },
)

DataGovJSONField = TypedDict(
    "DataGovJSONField",
    {
        "type": str,
        "id": str,
    },
)

DataGovJSONResult = TypedDict(
    "DataGovJSONResult",
    {
        "resource_id": str,
        "fields": list[DataGovJSONField],
        "records": list[dict[str, Any]],
        "_links": DataGovJSONLinks,
        "total": int,
        "limit": int,
    },
)


DataGovJSON = TypedDict(
    "DataGovJSON",
    {
        "help": str,
        "success": bool,
        "result": DataGovJSONResult,
    },
)

DataGovJSONValidator = TypeAdapter(DataGovJSON)

SingStatJSONColumnLeaf = TypedDict(
    "SingStatJSONColumnLeaf",
    {
        "key": str,
        "value": str,
    },
)

SingStatJSONColumnParent = TypedDict(
    "SingStatJSONColumnParent",
    {
        "key": str,
        "columns": list["SingStatJSONColumn"],
    },
)

SingStatJSONColumn: TypeAlias = SingStatJSONColumnParent | SingStatJSONColumnLeaf

SingStatJSONRow = TypedDict(
    "SingStatJSONRow",
    {
        "rowText": str,
        "columns": list[SingStatJSONColumn],
    },
)

SingStatJSONData = TypedDict(
    "SingStatJSONData",
    {
        "id": str,
        "title": str,
        "row": list[SingStatJSONRow],
    },
)

SingStatJSON = TypedDict(
    "SingStatJSON",
    {
        "Data": SingStatJSONData,
        "DataCount": int,
        "StatusCode": int,
        "Message": str,
    },
)

SingStatJSONValidator = TypeAdapter(SingStatJSON)

WorldBankJSON = list[dict[str, Any]]

WorldBankJSONValidator = TypeAdapter(WorldBankJSON)

import asyncio
import json
import os.path
from argparse import ArgumentParser, Namespace
from typing import Awaitable, Optional

import aiofiles

import fetcher.fetch
from fetcher.datasets import DEFAULT_DATASETS, Dataset, Source


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description="Fetch a dataset from data.gov.sg, SingStat or the World Bank."
    )

    subparsers = parser.add_subparsers(
        required=True, help="The operation mode", dest="operation"
    )

    default_subparser = subparsers.add_parser(
        "default", help="Fetch the default datasets"
    )
    default_subparser.add_argument(
        "-d", "--output-dir", type=str, help="The output directory"
    )

    single_subparser = subparsers.add_parser("single", help="Fetch a specified dataset")

    single_subparser.add_argument(
        "source",
        choices=["datagov", "singstat", "worldbank"],
        type=str,
        help="The source of the dataset",
    )

    single_subparser.add_argument(
        "dataset_id", metavar="dataset-id", type=str, help="The dataset identifier"
    )

    single_subparser.add_argument("-o", "--output", type=str, help="The output path")

    return parser.parse_args()


async def fetch_single(dataset: Dataset, output_path: Optional[str] = None) -> None:
    if not output_path:
        output_path = f"{dataset.id}.json"

    data = (
        await fetcher.fetch.fetch_datagov_dataset(dataset.id)
        if dataset.source == Source.DataGov
        else (
            await fetcher.fetch.fetch_singstat_dataset(dataset.id)
            if dataset.source == Source.SingStat
            else await fetcher.fetch.fetch_worldbank_dataset({dataset.id: dataset.id})
        )
    )

    async with aiofiles.open(output_path, "w") as file:
        json_str: str = json.dumps(data, indent=2)
        await file.write(json_str)
        print(f"Data successfully written to: {output_path}")


async def fetch_default(output_dir: Optional[str] = None) -> None:
    if not output_dir:
        output_dir = "default-datasets"

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    tasks: list[Awaitable] = []
    for name, dataset in DEFAULT_DATASETS.items():
        task = fetch_single(
            dataset,
            output_path=os.path.join(output_dir, f"{name}.json"),
        )
        tasks.append(task)

    await asyncio.gather(*tasks)


async def main() -> None:
    args = parse_args()
    if args.operation == "default":
        await fetch_default(output_dir=args.output_dir)
    else:
        source: Source = (
            Source.DataGov
            if args.source == "datagov"
            else (Source.SingStat if args.source == "singstat" else Source.WorldBank)
        )
        dataset: Dataset = Dataset(source, args.dataset_id)
        await fetch_single(dataset, output_path=args.output)


def entry() -> None:
    asyncio.run(main())

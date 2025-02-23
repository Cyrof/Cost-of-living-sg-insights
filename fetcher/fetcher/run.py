import json
import os.path
from argparse import ArgumentParser, Namespace
from typing import Optional

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


def fetch_single(dataset: Dataset, output_path: Optional[str] = None) -> None:
    if not output_path:
        output_path = f"{dataset.id}.json"

    data = (
        fetcher.fetch.fetch_datagov_dataset(dataset.id)
        if dataset.source == Source.DataGov
        else (
            fetcher.fetch.fetch_singstat_dataset(dataset.id)
            if dataset.source == Source.SingStat
            else fetcher.fetch.fetch_worldbank_dataset({dataset.id: dataset.id})
        )
    )

    with open(output_path, "w") as file:
        json.dump(data, file, indent=2)
        print(f"Data successfully written to: {output_path}")


def fetch_default(output_dir: Optional[str] = None) -> None:
    if not output_dir:
        output_dir = "default-datasets"

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for name, dataset in DEFAULT_DATASETS.items():
        fetch_single(
            dataset,
            output_path=os.path.join(output_dir, f"{name}.json"),
        )


def main() -> None:
    args = parse_args()
    if args.operation == "default":
        fetch_default(output_dir=args.output_dir)
    else:
        source: Source = (
            Source.DataGov
            if args.source == "datagov"
            else (Source.SingStat if args.source == "singstat" else Source.WorldBank)
        )
        dataset: Dataset = Dataset(source, args.dataset_id)
        fetch_single(dataset, output_path=args.output)

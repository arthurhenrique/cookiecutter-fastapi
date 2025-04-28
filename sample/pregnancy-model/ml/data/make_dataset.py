# -*- coding: utf-8 -*-
import click
from pathlib import Path

from loguru import logger
from dotenv import find_dotenv, load_dotenv


def pipeline():
    logger.info("Start making dataset.")


@click.command()
@click.argument("input_filepath", default="data/raw", type=click.Path(exists=True))
@click.argument("output_filepath", default="data/interim", type=click.Path())
def main(input_filepath, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger.info(f"Read from {input_filepath}, write to {output_filepath}.")


if __name__ == "__main__":

    load_dotenv(find_dotenv())

    # pylint: disable = no-value-for-paramete
    main()

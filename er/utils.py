from pathlib import Path

import pandas as pd
import yaml


def read_yaml_file(filename):
    """
    Reads a YAML file and returns its contents as a Python dictionary.

    Args:
      filename: The path to the YAML file.

    Returns:
      A Python dictionary containing the data from the YAML file.
    """
    with open(filename) as file:
        data = yaml.safe_load(file)
    return data


def get_data():
    """Grab data."""

    DATA_FILENAME = Path(__file__).parent / "config.yml"
    df = read_yaml_file(DATA_FILENAME)

    return df

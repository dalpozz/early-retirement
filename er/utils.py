from pathlib import Path

import numpy as np
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
    cfg = read_yaml_file(DATA_FILENAME)

    return cfg


def format_100k(number):
    """
    Formats a number with a separator for 100,000.

    Args:
      number: The number to format.

    Returns:
      The formatted number string.
    """
    if number >= 100000:
        return f"{number / 1000:.2f}k"  # Divide by 1000 and format with 2 decimal places
    else:
        return str(number)

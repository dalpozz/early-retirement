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


def future_value_annuity(rate, nper, pmt):
    """
    Calculates the future value of an ordinary annuity.

    Args:
      rate: The interest rate per period.
      nper: The total number of periods.
      pmt: The periodic payment.

    Returns:
      The future value of the annuity.
    """
    return pmt * (((1 + rate) ** nper) - 1) / rate


# Example usage:
rate = 0.05  # 5% annual interest rate
nper = 10  # Number of years
pmt = 1000  # Annual payment

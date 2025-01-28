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
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    DATA_FILENAME = Path(__file__).parent / "config.yml"
    df = read_yaml_file(DATA_FILENAME)

    return df

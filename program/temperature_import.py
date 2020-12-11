"""CSC110 Project -- Importing Temperature Data"""

import csv
from os import path
import pandas as pd


def df_temp(filepath: str) -> pd.DataFrame:
    """Return a dataframe representing the temperature data, containing the year as the first
    day in the year, and the raw and smoothed data points.

    Preconditions:
        - path.exists(filepath)
        - os.path.splitext(filepath)[1] == '.csv'

    >>> path = '../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    >>> df = df_temp(path)
    >>> dict(df.iloc[88])
    {'year': 1968.0, 'raw': -0.08, 'smoothed': -0.03}
    """
    return pd.read_csv(filepath, header=0,
                       names=['Year', 'Raw', 'Smoothed'])


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['csv', 'os', 'python_ta.contracts', 'pandas'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

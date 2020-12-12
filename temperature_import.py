"""CSC110 Project -- Importing Temperature Data"""

import csv
from os import path
import pandas as pd


def df_temp(filepath: str) -> pd.DataFrame:
    """Given a filepath referring to a .csv file with the correct format, return a dataframe
    representing the temperature data, containing year, raw, and smoothed data columns.

    Preconditions:
        - path.exists(filepath)
        - os.path.splitext(filepath)[1] == '.csv'

    >>> path = 'data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    >>> df_temp(path)
         Year   Raw  Smoothed
    0    1880 -0.15     -0.08
    1    1881 -0.07     -0.12
    2    1882 -0.10     -0.15
    3    1883 -0.16     -0.19
    4    1884 -0.27     -0.23
    ..    ...   ...       ...
    135  2015  0.90      0.83
    136  2016  1.02      0.87
    137  2017  0.93      0.91
    138  2018  0.85      0.95
    139  2019  0.99      0.99
    <BLANKLINE>
    [140 rows x 3 columns]
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

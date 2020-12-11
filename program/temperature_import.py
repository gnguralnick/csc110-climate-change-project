"""CSC110 Project -- Importing Temperature Data"""

import csv
from os import path
from dataclasses import dataclass
from typing import Dict
import pandas as pd


@dataclass
class TemperatureData:
    """A year of land-ocean temperature index data.

    Instance Attributes:
        - year: the year that the data is from, stored as the first day from that year
        - raw: the raw land-ocean temperature index for the year
        - smoothed: the smoothed land-ocean temperature index value for the year


    Representation Invariants:
        - 0 < self.year
    """
    year: int
    raw: float
    smoothed: float


def import_as_dict(filepath: str) -> Dict[int, TemperatureData]:
    """Import the temperature data from a csv file, and return it as a dictionary of the first
    day of the year of the data to the data as a TemperatureData dataclass.

    Preconditions:
        - path.exists(filepath)

    >>> PATH = '../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    >>> import_as_dict(PATH)[1904]
    TemperatureData(year=1904, raw=-0.47, smoothed=-0.3)
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        return {int(row[0]): TemperatureData(int(row[0]), float(row[1]), float(row[2]))
                for row in reader}


def import_as_dataframe(filepath: str) -> pd.DataFrame:
    """Return a dataframe representing the temperature data, containing the year as the first
    day in the year, and the raw and smoothed data points.

    Preconditions:
        - path.exists(filepath)

    >>> path = '../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    >>> df = import_as_dataframe(path)
    >>> dict(df.iloc[88])
    {'year': 1968.0, 'raw': -0.08, 'smoothed': -0.03}
    """
    return pd.read_csv(filepath, header=0,
                       names=['Year', 'Raw', 'Smoothed'])


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['csv', 'os', 'dataclasses', 'python_ta.contracts', 'pandas'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

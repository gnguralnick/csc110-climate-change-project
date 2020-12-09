"""CSC110 Project, Snowfall Import
"""

import csv
from os import path
from dataclasses import dataclass
from typing import Dict
import datetime
import pandas as pd


@dataclass
class TemperatureData:
    """A year of land-ocean temperature index data.

    Instance Attributes:
        - year: the year that the data is from, stored as the first day from that year
        - raw: the raw land-ocean temperature index for the year
        - smoothed: the smoothed land-ocean temperature index value for the year
    """
    year: datetime.date
    raw: float
    smoothed: float


def import_as_dict(filepath: str) -> Dict[datetime.date, TemperatureData]:
    """Import the temperature data from a csv file, and return it as a dictionary of the first
    day of the year of the data to the data as a TemperatureData dataclass.

    Preconditions:
        - path.exists(filepath)

    >>> PATH = '../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    >>> import_as_dict(PATH)[datetime.date(1904, 1, 1)]
    TemperatureData(year=datetime.date(1904, 1, 1), raw=-0.47, smoothed=-0.3)
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        return {first_date_in_year(row[0]): TemperatureData(first_date_in_year(row[0]),
                                                            float(row[1]), float(row[2]))
                for row in reader}


def import_as_dataframe(filepath: str) -> pd.DataFrame:
    """Return a dataframe representing the temperature data, containing the year as the first
    day in the year, and the raw and smoothed data points.

    Preconditions:
        - path.exists(filepath)

    >>> PATH = '../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    >>> df = import_as_dataframe(PATH)
    >>> dict(df.iloc[88])
    {'year': datetime.date(1968, 1, 1), 'raw': -0.08, 'smoothed': -0.03}
    """
    return pd.read_csv(filepath, header=0,
                       names=['year', 'raw', 'smoothed'], converters={'year': first_date_in_year})


def first_date_in_year(year: str) -> datetime.date:
    """Return the first day in a given string integer year.

    Preconditions:
        - 0 < int(year) < 10000

    >>> first_date_in_year('1')
    datetime.date(1, 1, 1)
    >>> first_date_in_year('2020')
    datetime.date(2020, 1, 1)
    """
    return datetime.date(int(year), 1, 1)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['csv', 'os', 'dataclasses', 'datetime', 'python_ta.contracts', 'pandas'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod(verbose=True)

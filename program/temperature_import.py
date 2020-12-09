"""CSC110 Project, Snowfall Import
"""

import csv
from os import path
from dataclasses import dataclass
from typing import Dict
import datetime


@dataclass
class TemperatureData:
    """A year of land-ocean temperature index data

    Instance Attributes:
        - year: the year that the data is from, stored as the first day from that year
        - raw: the raw land-ocean temperature index for the year
        - smoothed: the smoothed land-ocean temperature index value for the year
    """
    year: datetime.date
    raw: float
    smoothed: float


def import_temperature_data_dict(filepath: str) -> Dict[datetime.date, TemperatureData]:
    """Imports the temperature data from a csv file, and returns it as a dictionary of the first
    day of the year of the data to the

    Preconditions:
        - path.exists(filepath)

    >>> PATH = '../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    >>> import_temperature_data_dict(PATH)[datetime.date(1904, 1, 1)]
    TemperatureData(year=datetime.date(1904, 1, 1), raw=-0.47, smoothed=-0.3)
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        return {datetime.date(int(row[0]), 1, 1): TemperatureData(datetime.date(int(row[0]), 1, 1),
                                                                  float(row[1]), float(row[2]))
                for row in reader}


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['csv', 'os', 'dataclasses', 'datetime', 'python_ta.contracts'],
        'allowed-io': ['import_temperature_data_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod(verbose=True)

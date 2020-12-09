"""CSC110 Project, Snowfall Import
"""

import csv
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

DATA_FILEPATH = '../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'

def import_temperature_data(filepath: str) -> Dict[datetime.date, TemperatureData]:
    """Imports the temperature data from a csv file,
    and returns it as a dictionary
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        return {datetime.date(int(row[0]), 1, 1):
                    TemperatureData(datetime.date(int(row[0]), 1, 1), float(row[1]), float(row[2]))
                for row in reader}

if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],     # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

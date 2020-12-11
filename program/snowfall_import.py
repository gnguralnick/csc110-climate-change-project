
from os import path
import pandas as pd
from dataclasses import dataclass
import math
from typing import List
import python_ta


def df_snow(filepath: str, parameters: List[str]) -> pd.DataFrame:
    """
    This function returns a dataframe containing the given parameters from the given csv file.
    Preconditions:
        - path.exists(filepath)
        -
        - len(parameters) >= 1

    (doctest goes here)

    """
    df_import = pd.read_csv(filepath)

    for col in df_import.columns:
        if not any(col == prm for prm in parameters):
            del df_import[col]

    return df_import


def agg_years(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function aggregates the snowfall data into yearly averages for each region.
    Preconditions:
        - df.empty == False
        - "Region" in df.columns
        - "Year" in df.columns
        - "RSI" in df.columns
    """
    agg_df = df.groupby(["Region", "Year"]).agg({"RSI": ['mean']}).reset_index()

    return agg_df


# python_ta.check_all(config={
#     'extra-imports': [],  # the names (strs) of imported modules
#     'allowed-io': [],     # the names (strs) of functions that call print/open/input
#     'max-line-length': 100,
#     'disable': ['R1705', 'C0200']
# })

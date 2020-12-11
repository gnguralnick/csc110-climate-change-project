"""CSC110 Project -- Importing Snowfall Data"""

from os import path
from typing import List
import pandas as pd


REGIONS = {'Northeast': ['PA', 'NY', 'ME', 'MA', 'CT', 'RI', 'VT', 'NJ', 'DE', 'MD', 'NH'],
           'Northern Rockies and Plains': ['MT', 'ND', 'SD', 'WY', 'NE'],
           'Ohio Valley': ['MO', 'IL', 'TN', 'WV', 'OH', 'IN', 'KY'],
           'South': ['KS', 'OK', 'MS', 'TX', 'AR', 'LA'],
           'Southeast': ['VA', 'NC', 'SC', 'AL', 'GA', 'FL'],
           'Upper Midwest': ['MN', 'IA', 'WI', 'MI']}


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


# def agg_years_mean(df: pd.DataFrame) -> pd.DataFrame:
#     """This function aggregates the snowfall data into yearly averages for each region.
#
#     Preconditions:
#         - df.empty == False
#         - "Region" in df.columns
#         - "Year" in df.columns
#         - "RSI" in df.columns
#     """
#     return df.groupby(['Year', 'Region'], as_index=False)[['RSI']].mean()


def agg_years(df: pd.DataFrame, method: callable) -> pd.DataFrame:
    """This function aggregates the snowfall data into yearly averages for each region.

    Preconditions:
        - df.empty == False
        - "Region" in df.columns
        - "Year" in df.columns
        - "RSI" in df.columns
    """
    return method(df.groupby(['Year', 'Region'], as_index=False)[['RSI']])


def regions_to_states(df: pd.DataFrame) -> pd.DataFrame:
    stateified_so_far = pd.DataFrame({'State': [], 'Year': [], 'Mean RSI': []})
    for index in range(len(df)):
        for state in REGIONS[df.iloc[index]['Region']]:
            stateified_so_far = stateified_so_far.append(
                pd.DataFrame({'State': [state], 'Year': [df.iloc[index]['Year']],
                              'RSI': [df.iloc[index]['RSI']]}))
    return stateified_so_far







# python_ta.check_all(config={
#     'extra-imports': [],  # the names (strs) of imported modules
#     'allowed-io': [],     # the names (strs) of functions that call print/open/input
#     'max-line-length': 100,
#     'disable': ['R1705', 'C0200']
# })


from os import path
import pandas as pd
from dataclasses import dataclass
import math
from typing import List
import python_ta


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


def agg_years(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function aggregates the snowfall data into yearly averages for each region.
    Preconditions:
        - df.empty == False
        - "Region" in df.columns
        - "Year" in df.columns
        - "RSI" in df.columns
    """
    # agg_df = df.groupby(["Region", "Year"]).agg(['mean']).reset_index()
    # agg_df['RSI'] = agg_df['RSI']['mean']
    #
    # return agg_df
    regions = set(df['Region'])
    years = set(df['Year'])
    region_list = []
    [region_list.extend(regions) for year in years]
    year_list = []
    [year_list.extend([year] * len(regions)) for year in years]
    print(region_list)
    print(year_list)
    mean_list = [df.query('Year == ' + str(year) + ' and Region == "' + str(region) + '"')[
                     'RSI'].mean()
                 for region in regions for year in years]
    print(mean_list)
    return pd.DataFrame({'Region': region_list, 'Year': year_list, 'Mean RSI': mean_list})


def stateify_data(df: pd.DataFrame) -> pd.DataFrame:
    stateified_so_far = pd.DataFrame({'State': [], 'Year': [], 'Mean RSI': []})
    # [[stateified = stateified.append(pd.DataFrame({'State': [state],
    #                                                'Year': [df.iloc[index]['Year']],
    #                                                'Mean RSI': [df.iloc[index]['Mean RSI']]}))
    # for state in REGIONS[df.iloc[index]['Region']]] for index in range(len(df))]
    for index in range(len(df)):
        for state in REGIONS[df.iloc[index]['Region']]:
            stateified_so_far = stateified_so_far.append(
                pd.DataFrame({'State': [state], 'Year': [df.iloc[index]['Year']],
                              'Mean RSI': [df.iloc[index]['Mean RSI']]}))
    return stateified_so_far







# python_ta.check_all(config={
#     'extra-imports': [],  # the names (strs) of imported modules
#     'allowed-io': [],     # the names (strs) of functions that call print/open/input
#     'max-line-length': 100,
#     'disable': ['R1705', 'C0200']
# })

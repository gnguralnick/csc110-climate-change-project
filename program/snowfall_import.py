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
    """Return a dataframe containing the given parameters from the given csv file.

    Preconditions:
        - path.exists(filepath)
        - os.path.splitext(filepath)[1] == '.csv'
        - len(parameters) >= 1

    >>> path = '../data/snowfall/regional-snowfall-index_c20191218.csv'
    >>> df_snow(path, ['Region', 'Year', 'RSI'])
                               Region     RSI  Year
    0                        National   0.000  2019
    1                       Northeast   2.386  2019
    2     Northern Rockies and Plains   3.608  2019
    3                     Ohio Valley   0.151  2019
    4                       Southeast   0.428  2019
    ...                           ...     ...   ...
    4377  Northern Rockies and Plains   0.542  1900
    4378                  Ohio Valley   9.488  1900
    4379                        South  10.964  1900
    4380                    Southeast   0.000  1900
    4381                Upper Midwest   3.593  1900
    <BLANKLINE>
    [4382 rows x 3 columns]
    """
    df_import = pd.read_csv(filepath)

    for col in df_import.columns:
        if not any(col == prm for prm in parameters):
            del df_import[col]

    return df_import


def remove_national(df: pd.DataFrame) -> pd.DataFrame:
    """Remove columns where 'Region' == National.

    Preconditions
        - df.empty == False
        - 'Region' in df.columns

    >>> data = {'Region': ['National', 'South'], 'Year': [2001, 2001], 'RSI': [3.0, 2.15]}
    >>> df = pd.DataFrame(data)
    >>> remove_national(df)
      Region  Year   RSI
    1  South  2001  2.15
    """
    return df.query('Region != "National"')


def agg_years(df: pd.DataFrame, method: callable) -> pd.DataFrame:
    """This function aggregates the snowfall data by year and region, given a method of
    DataFrameGroupBy.

    Preconditions:
        - df.empty == False
        - 'Region' in df.columns
        - 'Year' in df.columns
        - 'RSI' in df.columns
        - hasattr(pd.core.groupby.generic.DataFrameGroupBy, method.__name__)
    """
    return method(df.groupby(['Year', 'Region'], as_index=False)[['RSI']])


def regions_to_states(df: pd.DataFrame) -> pd.DataFrame:
    """Convert a dataframe with a regions column to a dataframe with a states column containing
    the same data, but with duplicated data points for each state in the regions.

    Preconditions
        - df.empty == False
        - 'Region' in df.columns
        - 'Year' in df.columns
        - 'RSI' in df.columns

    >>> data = {'Region': ['Northeast', 'South'], 'Year': [2001, 2001], 'RSI': [3.0, 2.15]}
    >>> df = pd.DataFrame(data)
    >>> regions_to_states(df)
      State    Year   RSI
    0    PA  2001.0  3.00
    0    NY  2001.0  3.00
    0    ME  2001.0  3.00
    0    MA  2001.0  3.00
    0    CT  2001.0  3.00
    0    RI  2001.0  3.00
    0    VT  2001.0  3.00
    0    NJ  2001.0  3.00
    0    DE  2001.0  3.00
    0    MD  2001.0  3.00
    0    NH  2001.0  3.00
    0    KS  2001.0  2.15
    0    OK  2001.0  2.15
    0    MS  2001.0  2.15
    0    TX  2001.0  2.15
    0    AR  2001.0  2.15
    0    LA  2001.0  2.15
    """
    states_so_far = pd.DataFrame({'State': [], 'Year': [], 'RSI': []})
    for index in range(len(df)):
        for state in REGIONS[df.iloc[index]['Region']]:
            states_so_far = states_so_far.append(
                pd.DataFrame({'State': [state], 'Year': [df.iloc[index]['Year']],
                              'RSI': [df.iloc[index]['RSI']]}))
    return states_so_far


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['os', 'python_ta.contracts', 'pandas'],
        'allowed-io': ['df_snow'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

"""CSC110 Project -- Processing Data"""

from typing import List
import pandas as pd


def intersecting_years(df_list: List[pd.DataFrame]) -> List[pd.DataFrame]:
    """Given a list of DataFrames with a continuous 'Year' column, return a list containing the same
    DataFrames with any years that are not present in the others removed.

    Preconditions:
        - df.empty == False
        - 'Year' in df.columns

    >>> data1 = {'Region': ['National', 'South'], 'Year': [2001, 2001], 'RSI': [3.0, 2.15]}
    >>> data2 = {'Year': [2001, 2002], 'Raw': [0.5, 0.8], 'Smoothed': [0.5, 0.7]}
    >>> df1 = pd.DataFrame(data1)
    >>> df2 = pd.DataFrame(data2)
    >>> intersecting_years([df1, df2])
    [     Region  Year   RSI
    0  National  2001  3.00
    1     South  2001  2.15,    Year  Raw  Smoothed
    0  2001  0.5       0.5]
    """
    upper_bound = min(max(df['Year']) for df in df_list)
    lower_bound = max(min(df['Year']) for df in df_list)

    return [df.query(str(upper_bound) + ' >= Year >= ' + str(lower_bound)) for df in df_list]


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
